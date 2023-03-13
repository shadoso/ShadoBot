from datetime import datetime
from abs_pth import root_path
from telegram import Bot as ErrorBot
from config.config import settings
import json


class TelegramWarning:
    def __init__(self, error, command_name: str, command_type: str):
        self.__error = str(error).split(":")
        self.__command_name = command_name
        self.__command_type = command_type

    async def get_error_details(self):
        path = ["app", "main", "error_handling", "text", "error.json"]

        key = self.__error[1].strip() + f"-{self.__command_name.capitalize()}"
        text = f"{datetime.today()}\n{key}\n{':'.join(self.__error[len(self.__error) - 2::]).strip()}\n{self.__command_type}"
        file = root_path(where=path)

        with open(file=file, mode="r") as error_counter:
            counter = json.load(error_counter)
            if key not in counter.keys():
                counter[key] = 1

            else:
                counter[key] += 1

        with open(file=file, mode="w") as error_writing:
            error_writing.write(json.dumps(counter, indent=2))

        return text, counter[key]

    async def warning_trigger(self):
        message, trigger = await self.get_error_details()
        if trigger % 15 == 1:
            warning = ErrorBot(token=settings.TELEGRAM_API)
            await warning.send_message(chat_id=settings.TELEGRAM_CHAT_ID, text=message)
        else:
            return
