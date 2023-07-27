# csv/xlsx to database

import pandas as pd
import mysql.connector
import openpyxl

# this script corresponds to setting  up a basic MySQL database from the dataset

# database credentials
user = 'root'
password = 'root'
schema = 'chatbot'


# creates schema
def create_database():
    db_connection = mysql.connector.connect(user=user, password=password,
                                            host='127.0.0.1')
    db_cursor = db_connection.cursor()
    create_schema_query = f"CREATE SCHEMA {schema}"
    db_cursor.execute(create_schema_query)
    db_connection.commit()
    db_cursor.close()
    db_connection.close()


# creates the table from the dataset
def setup_database(from_file):
    # reading the dataset
    if from_file.endswith('.csv'):
        data = pd.read_csv(from_file)
    else:
        data = pd.read_excel(from_file)

    table_name = "dataset_small"

    db_connection = mysql.connector.connect(user=user, password=password,
                                            host='127.0.0.1',
                                            database=schema)
    db_cursor = db_connection.cursor()

    # cleaning up dataset data and adjusting it for MySQL
    data.columns = data.columns.str.replace('.', '_')
    data.columns = data.columns.str.replace("blamming_yourself", "blaming_yourself")
    data = data.replace({'yes': 1, 'no': 0, "anexiety": "anxiety", "bipolar": "bipolar disorder",
                         "psychotic deprission": "psychotic depression",
                         "Loneliness": "loneliness"})
    data_types = {
        column: 'INT' if column != 'Disorder' else 'VARCHAR(255)'
        for column in data.columns
    }

    # creating the table query is composed based on the data columns in the dataset
    create_table_query = f"CREATE TABLE {table_name} ({', '.join([f'{column} {data_types[column]}' for column in data.columns])})"

    print(create_table_query)
    db_cursor.execute(create_table_query)

    # inserts data from the dataset into the table
    for _, row in data.iterrows():
        values = ','.join([f"'{str(value)}'" for value in row])
        insert_query = f"INSERT INTO {table_name} VALUES ({values})"
        db_cursor.execute(insert_query)

    db_connection.commit()
    db_cursor.close()
    db_connection.close()

# this code is only needed to run once
# create_database()
# setup_database("../resources/data/dataset_small.xlsx")
# setup_database("resources\dataset_big.csv")
