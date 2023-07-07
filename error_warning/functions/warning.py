from datetime import datetime
from telegram import Bot as ErrorBot
from config.config import settings
import json
from absolute_path import list_to_path

WARNING_ = list_to_path(file_path=["error_warning", "text", "error.json"])


async def error_details(error: str, command_name: str, command_type: str):
    error_format = [detail.strip() for detail in error.split(":")[-2:]]
    date = datetime.today().strftime("%d/%m/%Y %H:%M")
    error_key = f"{error_format[0]}-{command_name.capitalize()}"
    message = f"{date}\n{error_key}\n{': '.join(error_format)}\n{command_type}\n{error}"
    return error_key, message


async def warning_trigger(error_key: str, message: str):
    with open(file=WARNING_, mode="r") as error_counter:
        token = json.load(error_counter)

        if error_key not in token.keys():
            token[error_key] = 1

        else:
            token[error_key] += 1

    with open(file=WARNING_, mode="w") as error_writing:
        error_writing.write(json.dumps(token, indent=2))

    if token[error_key] % 15 == 1:
        warning = ErrorBot(token=settings.TELEGRAM_API)
        await warning.send_message(chat_id=settings.TELEGRAM_CHAT_ID, text=message)

    else:
        return None
