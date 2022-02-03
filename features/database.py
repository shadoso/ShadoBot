import psycopg2

HOST_NAME = 'localhost'
DATABASE = 'BOT'
USER_NAME = 'postgres'
PASSWORD = 'shadobot'
PORT_ID = 5432
DESCRIPTION = 'Uma descrição, chamada descrição'
DEED = 'Criou uma conta no Shadosoverso'
CASH = 9945.95


class Manager:
    def __init__(self, user_id, user_name):
        self.conn = psycopg2.connect(host=HOST_NAME, dbname=DATABASE, user=USER_NAME, password=PASSWORD, port=PORT_ID)
        self.cur = self.conn.cursor()
        self.user_id = user_id
        self.user_name = user_name

    def verify_user(self):
        pass

    def create_user(self):
        discord_user = '''
        INSERT INTO users (discord_id, discord_name, description, deed_1, shadocoin) VALUES (%s, %s,%s, %s, %s)
        '''
        user_values = (self.user_id, self.user_name, DESCRIPTION, DEED, CASH)
        self.cur.execute(discord_user, user_values)
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        return 'Done'

    def update_user(self):
        pass
