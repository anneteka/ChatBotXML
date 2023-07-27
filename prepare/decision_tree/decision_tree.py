import pandas as pd
from sklearn.tree import *
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import mysql.connector
import xml.etree.ElementTree as ET
from prepare.decision_tree import decision_tree_processing

user = 'root'
password = 'root'
schema = 'chatbot'


# this method builds the decision tree with the sklearn library
def get_decision_tree(symptoms=None):
    if symptoms is None:
        symptoms = []
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user=user,
        password=password,
        database=schema
    )

    query = "SELECT * FROM dataset_small"
    # if no symptoms were received then selects the whole dataset
    # otherwise selects rows with specified symptoms present
    if symptoms:
        query = query + " WHERE "
        for i in range(len(symptoms) - 1):
            query = query + symptoms[i] + " = 1 and "
        query = query + symptoms[len(symptoms) - 1] + " = 1"

    dataset = pd.read_sql(query, conn)

    conn.close()

    X = dataset.iloc[:, 1:-1]
    y = dataset['Disorder']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # print(X_test)
    decision_tree = DecisionTreeClassifier(splitter="random", max_features="log2", min_samples_leaf=1)
    decision_tree.fit(X_train, y_train)
    y_pred = decision_tree.predict(X_test)
    # accuracy = accuracy_score(y_test, y_pred)
    # print('Accuracy:', accuracy)
    return decision_tree


# retruns the decision tree as an xml string. see /resources/chatbot/decision_tree_example.xml for an example output
def get_decision_tree_text(symptoms=None):
    decision_tree = get_decision_tree(symptoms)
    tree_xml = decision_tree_processing.decision_tree_to_xml(decision_tree[0], feature_names=decision_tree[2],
                                                             class_names=decision_tree[0].classes_)
    return tree_xml
