#Migration postgres to mysql
import os
import psycopg2
import MySQLdb

PG = {
    'name' : 'frgc2',
    'user' : 'postgres',
    'pass' : 'password',
    'host' : 'localhost',
}

MYSQL = {
    'db': 'frgc2',
    'user': 'user',
    'passwd': 'password',
    'host': 'localhost',
}

TABLES_LIST = [
    'collection',
    'config',
    'contact',
    'contactprefix',
    'emotiontype',
    'env_illuminant',
    'env_sensor',
    'env_stage',
    'environment',
    'food',
    'frame_desc',
    'haircolor',
    'illuminant',
    'illuminant_types',
    'illuminantcolor'
    'medication',
    'race_list',
    'rec_frame',
    'rec_illuminant',
    'rec_sensor',
    'rec_sub_collection'
    'rec_sub_face',
    'rec_sub_gait',
    'rec_sub_iris',
    'rec_sub_novel',
    'rec_sub_stage',
    'rec_subject',
    'recording',
    'recordingformat',
    'sensor',
    'sensormedia',
    'stage',
    'stage_seg',
    'subject'
]

def create_pg_connection():
    string = "dbname={name} user={user} password={pass}".format(**PG)
    conn = psycopg2.connect(string)
    cur = conn.cursor()
    return cur

def generate_tsv(table):
    file_ = open('/tmp/{0}.tsv'.format(table), 'w')
    kwargs = {
        'file': file_,
        'table': table,
    }
    cursor = create_pg_connection()
    cursor.copy_to(**kwargs)
    cursor.close()

def import_tsv(table):
    MYSQL.update({'table': table})
    mysql_command = 'mysqlimport --local --compress --user={user} --password={passwd} --verbose --host={host} {db} /tmp/{table}.tsv'.format(**MYSQL)
    os.system(mysql_command)

def create_mysql_connection():
    conn = MySQLdb.connect(**MYSQL)
    cursor = conn.cursor()
    return cursor

def get_mysql_tables():
    cursor = create_mysql_connection()
    cursor.execute(""" SHOW TABLES """)
    result = cursor.fetchall()
    for table in result:
        yield table[0]


if __name__=="__main__":
    TABLES_LIST = []
    for table in get_mysql_tables():
        TABLES_LIST.append(table)
    for table in TABLES_LIST:
        generate_tsv(table)
        import_tsv(table)