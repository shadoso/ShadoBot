import psycopg2

HOST_NAME = 'localhost'
DATABASE = 'BOT'
USER_NAME = 'postgres'
PASSWORD = 'shadobot'
PORT_ID = 5432

conn = psycopg2.connect(
    host=HOST_NAME,
    dbname=DATABASE,
    user=USER_NAME,
    password=PASSWORD,
    port=PORT_ID
)
cur = conn.cursor()

tag_type = '''
    CREATE TYPE tag AS ENUM (
    'Otaku', 'Profit', 'Lucky')
'''

cur.execute()

conn.commit()

cur.close()
conn.close()
