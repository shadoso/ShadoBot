import psycopg2
import decimal

# Postgres info -------------------------------------------------------
HOST_NAME = 'localhost'
DATABASE = 'BOT'
USER_NAME = 'postgres'
PASSWORD = 'shadobot'
PORT_ID = 5432
# Postgres commands ---------------------------------------------------
CREATE_USER = 'INSERT INTO users (discord_id, discord_name, description, deed_1, shadocoin) VALUES (%s, %s,%s, %s, %s)'
QUERY_USER = 'SELECT * FROM users WHERE discord_id = '
UPDATE_CASH1 = 'UPDATE users SET shadocoin = '
UPDATE_CASH2 = ' WHERE discord_id = '
# Default user info ---------------------------------------------------
DESCRIPTION = 'Uma descrição, chamada descrição'
DEED = 'Criou uma conta no Shadosoverso'
CASH = 945.00
MAX_CASH = 95994599459945.45


class Manager:
    def __init__(self, user_id, user_name):
        self.conn = psycopg2.connect(host=HOST_NAME, dbname=DATABASE, user=USER_NAME, password=PASSWORD, port=PORT_ID)
        self.cur = self.conn.cursor()
        self.user_id = user_id
        self.user_name = user_name

    def verify_user(self):
        """
        :return: None if user doesn't exist, else return user data
        """
        self.cur.execute(QUERY_USER + str(self.user_id))
        data = self.cur.fetchall()
        return None if len(data) == 0 else data

    def close_query(self):
        self.cur.close()
        self.conn.close()
        return 'Closed'

    def create_user(self):
        user_values = (self.user_id, self.user_name, DESCRIPTION, DEED, CASH)
        self.cur.execute(CREATE_USER, user_values)
        self.conn.commit()
        return 'Created'

    def update_cash(self, cash):
        self.cur.execute(UPDATE_CASH1 + cash + UPDATE_CASH2 + self.user_id)
        self.conn.commit()
        return 'Updated'
