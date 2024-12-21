import sqlite3
import os

location = os.path.abspath(os.path.join(os.path.dirname(__file__), '../database/main.db'))

def dbconnect():
    return sqlite3.connect(location)

def execute_query(query):
    connection = dbconnect()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()


def get_result_from_query(query):
    connection = dbconnect()
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result