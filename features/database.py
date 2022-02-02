import psycopg2

HOST_NAME = 'localhost'
DATABASE = 'BOT'
USER_NAME = 'postgres'
PASSWORD = 'shadobot'
PORT_ID = 5432


class Manager:
    def __init__(self, user_id, user_name):
        self.conn = psycopg2.connect(host=HOST_NAME, dbname=DATABASE, user=USER_NAME, password=PASSWORD, port=PORT_ID)
        self.port = 5432
        self.user_id = user_id
        self.user_name = user_name

    def verify_user(self):
        pass

    def create_user(self):
        pass

    def update_user(self):
        pass
