# csv/xlsx to database

import pandas as pd
import mysql.connector
import openpyxl


def setup_database(from_file):
    if from_file.endswith('.csv'):
        data = pd.read_csv(from_file)
    else:
        data = pd.read_excel(from_file)

    table_name = from_file.split('\\')[-1].split('.')[0]

    db_connection = mysql.connector.connect(user='root', password='root',
                                            host='127.0.0.1',
                                            database='chatbot')
    db_cursor = db_connection.cursor()

    data.columns = data.columns.str.replace('.', '_')
    data = data.replace({'yes': 1, 'no': 0})

    columns = ','.join(data.columns)
    data_types = {
        column: 'INT' if column != 'Disorder' else 'VARCHAR(255)'
        for column in data.columns
    }

    create_table_query = f"CREATE TABLE {table_name} ({', '.join([f'{column} {data_types[column]}' for column in data.columns])})"

    print(create_table_query)
    db_cursor.execute(create_table_query)

    for _, row in data.iterrows():
        values = ','.join([f"'{str(value)}'" for value in row])
        insert_query = f"INSERT INTO {table_name} VALUES ({values})"
        db_cursor.execute(insert_query)

    db_connection.commit()
    db_cursor.close()
    db_connection.close()


setup_database("resources\dataset_small.xlsx")
setup_database("resources\dataset_big.csv")

