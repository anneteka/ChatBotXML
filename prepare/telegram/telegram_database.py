# csv/xlsx to database

import pandas as pd
import mysql.connector
import openpyxl

user = 'root'
password = 'root'
schema = 'chatbot'


def create_table():
    db_connection = mysql.connector.connect(user=user, password=password,
                                            host='127.0.0.1',
                                            database=schema)
    db_cursor = db_connection.cursor()
    create_table_query = f"CREATE TABLE telegram_data (user_id int NOT NULL, current_node int, xml text, PRIMARY KEY (user_id))"
    db_cursor.execute(create_table_query)

    db_connection.commit()
    db_cursor.close()
    db_connection.close()


def create_user(user_id, xml_string):
    db_connection = mysql.connector.connect(user=user, password=password,
                                            host='127.0.0.1',
                                            database=schema)
    db_cursor = db_connection.cursor()
    try:
        insert_query = f"INSERT INTO telegram_data (user_id, current_node, xml) VALUES ({user_id}, -2, '{xml_string}')"
        db_cursor.execute(insert_query)
        db_connection.commit()
        db_cursor.close()
        db_connection.close()
    except:
        update_user(user_id, -2, xml_string)


def update_user(user_id, current_node=-2, xml=""):
    db_connection = mysql.connector.connect(user=user, password=password,
                                            host='127.0.0.1',
                                            database=schema)
    db_cursor = db_connection.cursor()

    set_text = ""
    if current_node != -2 and xml == "":
        set_text = "current_node = " + str(current_node)
    elif current_node == -2 and xml != "":
        set_text = "xml = '" + xml + "'"
    elif current_node != -2 and xml != "":
        set_text = "current_node = " + str(current_node) + ", xml = '" + str(xml) + "'"
    else:
        db_cursor.close()
        db_connection.close()
        return

    update_user_query = f"UPDATE telegram_data SET {set_text}  WHERE user_id = {user_id}"
    db_cursor.execute(update_user_query)

    db_connection.commit()
    db_cursor.close()
    db_connection.close()


def delete_user(user_id):
    db_connection = mysql.connector.connect(user=user, password=password,
                                            host='127.0.0.1',
                                            database=schema)
    db_cursor = db_connection.cursor()

    delete_user_query = f"DELETE FROM telegram_data WHERE user_id = {user_id}"

    db_cursor.execute(delete_user_query)

    db_connection.commit()
    db_cursor.close()
    db_connection.close()


def get_user(user_id):
    db_connection = mysql.connector.connect(user=user, password=password,
                                            host='127.0.0.1',
                                            database=schema)
    db_cursor = db_connection.cursor()

    select_user_query = f"SELECT * FROM telegram_data WHERE user_id = {user_id}"

    db_cursor.execute(select_user_query)
    res = db_cursor.fetchone()
    db_connection.commit()
    db_cursor.close()
    db_connection.close()

    return res

# create_user(12345, "<test>hello</test>")
# print(get_user(user_id=12345))
# update_user(12345, current_node=3)
# print(get_user(user_id=12345))
# update_user(12345, xml="<test>hello world</test>")
# print(get_user(user_id=12345))
# update_user(12345, current_node=4, xml="<test>hello world!</test>")
# print(get_user(user_id=12345))
# delete_user(12345)
