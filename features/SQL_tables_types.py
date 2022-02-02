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
tag_type = '''
    CREATE TYPE tag AS ENUM (
    '11FPS', ':unlock:', 'Profit', 'Otaku', 'Gamer');
'''
org_type = '''
    CREATE TYPE org AS ENUM (
    'Glimpsers', 'Embers', 'Cloud Benders', 'Absolvers', 'Cloud Drinkers');
'''
user_tables = '''
    CREATE TABLE IF NOT EXISTS  users (
    discord_id          long PRIMARY KEY
    discord_name        varchar(128),
    description         varchar(256),
    organization        org,
    house               house,
    tag                 tag,
    deed_1              varchar(56),
    deed_2              varchar(56),
    deed_3              varchar(56),
    itens               list,
    inventory           list,
    shadocoin           money,
    
    );
'''

cur = conn.cursor()
