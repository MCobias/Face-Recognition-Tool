#Connect to mysql server
import os
import MySQLdb

MYSQL = {
    'db': 'data_set_faces',
    'user': 'user',
    'passwd': 'password',
    'host': 'localhost',
}

CONFIG = {
    'race': 'all',
    'year_of_birth': 'all',
    'gender': 'all',
    'glasses': 'all',
    'emotion': 'all',
}

def create_mysql_connection():
    conn = MySQLdb.connect(**MYSQL)
    cursor = conn.cursor()
    return cursor

def create_query(name_table, config=CONFIG):
    query = "SELECT * FROM " + name_table
    if(config['race']!='all'):
        query += ""
    return query

def get_mysql_images(name_table):
    result_query = []
    try:
        cursor = create_mysql_connection()
        create_query(name_table)
        cursor.execute(create_query(name_table))
        row = cursor.fetchone()

        while row is not None:
            result_query.append(row)
            row = cursor.fetchone()

    except TypeError as e:
        print(e)

    finally:
        cursor.close()
        if(len(result_query)):
            return result_query
        else:
            return None
