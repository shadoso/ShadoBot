from datetime import datetime
import time
from telegram import Bot as ErrorBot
from config.config import settings
from collections import defaultdict
from absolute_path import list_to_path

WARNING_ = list_to_path(file_path=["errors", "warning", "text", "error.json"])

COUNT_ = "count"
LAST_REPORTED = "last_reported"

WARNING_BOT = ErrorBot(token=settings.TELEGRAM_API)

error_cache = defaultdict(
    lambda: {
        COUNT_: 0,
        LAST_REPORTED: None
    }
)

async def error_details(command_name: str, command_type: str, error):
    date = datetime.today().strftime("%d/%m/%Y %H:%M")
    message = f"{date}\n{command_name.capitalize()}: {command_type}\n{error}"
    error_key = f"{command_name}-"+ "-".join(str(error).split(":")[-2:]).replace("'", "")

    return error_key.replace(" ", ""),  message


async def error_trigger(error_key: str, message: str):
    error_threshold = 64
    error_time_limit = 512
    
    error_cache[error_key][COUNT_] += 1

    if not error_cache[error_key][LAST_REPORTED]:
        error_cache[error_key][LAST_REPORTED] = time.time()
        await WARNING_BOT.send_message(chat_id=settings.TELEGRAM_CHAT_ID, text=message)

    if error_cache[error_key][COUNT_] >= error_threshold and time.time() - error_cache[error_key][LAST_REPORTED] >=error_time_limit:
        message = f"{message}\nCount:{error_cache[error_key][COUNT_]}"

        #reset
        error_cache[error_key][COUNT_] = 0
        error_cache[error_key][LAST_REPORTED] = time.time()

        await WARNING_BOT.send_message(chat_id=settings.TELEGRAM_CHAT_ID, text=message)


