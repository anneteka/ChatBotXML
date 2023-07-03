import pandas as pd
from sklearn.tree import *
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import mysql.connector
import xml.etree.ElementTree as ET
from decision_tree_processing import *

user = 'root'
password = 'root'
schema = 'chatbot'


def get_decision_tree(dataset_name):
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
    # decision_tree = DecisionTreeClassifier(max_depth=20, splitter='random', min_samples_split=10)
    decision_tree = DecisionTreeClassifier()

    # Train the decision tree model
    decision_tree.fit(X_train, y_train)

    # Make predictions on the testing set
    y_pred = decision_tree.predict(X_test)

    # Calculate the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)
    print('Accuracy:', accuracy)

    tree_text = export_text(decision_tree, feature_names=list(X.columns))
    return decision_tree, tree_text, list(X.columns)


decision_tree = get_decision_tree("dataset_small")


tree_xml = decision_tree_to_xml(decision_tree[0], feature_names=decision_tree[2], class_names=decision_tree[0].classes_)

tree_xml.write('decision_tree.xml')
