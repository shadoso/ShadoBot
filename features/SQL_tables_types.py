import psycopg2

HOST_NAME = 'localhost'
DATABASE = 'BOT'
USER_NAME = 'postgres'
PASSWORD = 'shadobot'
PORT_ID = 5432

tag_type = '''
        CREATE TYPE tag AS ENUM (
        '11FPS', ':unlock:', 'Profit', 'Otaku', 'Gamer');
    '''
org_type = '''
        CREATE TYPE org AS ENUM (
        'Glimpsers', 'Embers', 'Cloud Benders', 'Cloud Drinkers', 'Absolvers');
    '''
user_tables = '''
        CREATE TABLE IF NOT EXISTS  users (
        discord_id          bigint PRIMARY KEY,
        discord_name        varchar(128),
        description         varchar(256),
        org                 org,
        percent             decimal[],
        tag                 tag,
        deed_1              varchar(56),
        deed_2              varchar(56),
        deed_3              varchar(56),
        itens               text[],
        inventory           text[],
        shadocoin           money
        );
    '''


conn = psycopg2.connect(
    host=HOST_NAME,
    dbname=DATABASE,
    user=USER_NAME,
    password=PASSWORD,
    port=PORT_ID
)

cur = conn.cursor()

cur.execute(user_tables)

conn.commit()
conn.close()
conn.close()
