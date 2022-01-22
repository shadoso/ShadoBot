import gspread
from key.tokens import user_sheets
from google.oauth2.service_account import Credentials


class Manager:
    def __init__(self, ids, name):
        scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
        credentials = Credentials.from_service_account_file(user_sheets(), scopes=scopes)
        gc = gspread.authorize(credentials)
        self.__open = gc.open("Shadobot").sheet1
        self.__ids = ids
        self.__name = name

    def create_user(self):
        row = [
            self.__ids,
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
            9.45,
        ]

        self.__open.insert_row(row, 2)
        return True

    def show_user(self):
        local = self.__open.find(self.__ids)
        row = local.row
        show = self.__open.row_values(row)

        return show


if __name__ == '__main__':
    account = Manager("292139416275779584", "Shadoso")
    print(account.show_user())
