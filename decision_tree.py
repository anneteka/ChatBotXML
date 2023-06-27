import pandas as pd
from sklearn.tree import *
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import mysql.connector
import xml.etree.ElementTree as ET

user = 'root'
password = 'root'
schema = 'chatbot'


def get_tree_text(dataset_name):
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user=user,
        password=password,
        database=schema
    )

    query = "SELECT * FROM " + dataset_name + ";"
    dataset = pd.read_sql(query, conn)

    conn.close()

    # Separate features (symptoms and age) and the target variable (disease)
    X = dataset.iloc[:, 1:-1]  # Features (symptoms and age)
    y = dataset['Disorder']  # Target variable


    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print(X_test)
    # Initialize the decision tree classifier with a maximum depth of 10
    decision_tree = DecisionTreeClassifier(max_depth=20, splitter='random', min_samples_split=10, max_features='log')

    # Train the decision tree model
    decision_tree.fit(X_train, y_train)

    # Make predictions on the testing set
    y_pred = decision_tree.predict(X_test)

    # Calculate the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)
    print('Accuracy:', accuracy)

    tree_text = export_text(decision_tree, feature_names=list(X.columns))
    return tree_text


def build_xml_tree(decision_tree, element):
    lines = decision_tree.split('\n')
    for line in lines:
        line = line.strip()
        print(line)
        if line:
            indent_level = line.count('|') - 1
            line = line.replace('|', '').strip()
            if 'class:' in line:
                class_name = line.split(':')[1].strip()
                ET.SubElement(element, 'Leaf', name=class_name)
            else:
                feature, threshold = line.split('<=') if '<=' in line else line.split('>')
                feature = feature.strip()
                threshold = threshold.strip()
                node_element = ET.SubElement(element, 'Node', name=feature)
                if '<=' in line:
                    ET.SubElement(node_element, 'Yes')
                else:
                    ET.SubElement(node_element, 'No')
                build_xml_tree(line[line.find('|') + 1:], node_element)


# Create the root element of the

# Build the XML tree recursively
root = ET.Element('DecisionTree')
decision_tree_text = get_tree_text("dataset_small")
# Build the XML tree recursively
# build_xml_tree(decision_tree_text, root)

# Create the XML tree
# xml_tree = ET.ElementTree(root)

# Save the XML tree to a file
# xml_tree.write('decision_tree.xml')

print(decision_tree_text)