import gspread
from google.oauth2.service_account import Credentials

SCOPE = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
PATH = "/home/bismutoso/PycharmProjects/ShadoBot/key/shadobot-key.json"
ROW = 2


class Manager:
    def __init__(self, discord_id, name):
        scopes = SCOPE
        credentials = Credentials.from_service_account_file(PATH, scopes=scopes)
        gc = gspread.authorize(credentials)

        self.__open = gc.open("Shadobot").sheet1
        self.__discord_id = discord_id
        self.__name = name

    def create_user(self):
        user = [
            self.__discord_id,
            self.__name,
            "Novo usuário",
            "None",
            "None",
            "Criou uma conta",
            "None",
            "None",
            "None",
            "None",
            "None",
            "None",
            9.45,
        ]

        self.__open.insert_row(user, ROW)
        return True

    def verify_user(self):
        local = self.__open.find(self.__discord_id)
        return True if local is not None else False

    def show_info(self):
        info = self.__open.find(self.__discord_id)
        return self.__open.row_values(info.row)
