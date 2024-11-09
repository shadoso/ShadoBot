import json
from pathlib import Path
from config.constants import ENCODED_UTF_8_
from json import load
from languages.excluded_languages import exclude
import aiofiles
import asyncio

TEXT_PATH = "text"
RESPONSE_JSON = "response.json"
DESCRIPTION_JSON = "description.json"
COMMANDS_PATH = "commands"


class Dotted(dict):
    __getattr__ = dict.__getitem__


def open_json(file_path: Path) -> dict:
    with open(file=file_path) as json_file:
        dictionary = load(json_file)

    return dictionary

def save_json(file_path: Path, file: dict):
    with open(file=file_path, mode="w", encoding=ENCODED_UTF_8_) as json_file:
        json.dump(obj=file, fp=json_file, ensure_ascii=False, indent=2)


async def ai_json(new_json: dict):
    # Lê o conteúdo existente do arquivo, se existir
    async with aiofiles.open("/home/bismuto/PycharmProjects/ShadoBot/cogs/commands/shadobot/data/data.json", mode='r', encoding='utf-8') as json_file:
        contents = await json_file.read()
        data = json.loads(contents) if contents else []

    # Adiciona o novo JSON à lista existente, no formato esperado
    if isinstance(new_json, dict) and "messages" in new_json:
        data.append(new_json)
    else:
        raise ValueError("Formato inválido! O JSON precisa conter a chave 'messages'.")

    # Salva a lista atualizada de volta no arquivo
    async with aiofiles.open("/home/bismuto/PycharmProjects/ShadoBot/cogs/commands/shadobot/data/data.json", mode='w', encoding='utf-8') as json_file:
        await json_file.write(json.dumps(data, ensure_ascii=False, indent=2))




def excluded_languages(dictionary: dict, exclude_list: list) -> dict:
    new_dictionary = {}

    for key, value_or_dict in dictionary.items():
        if key not in exclude_list:
            if isinstance(value_or_dict, dict):
                new_dictionary[key] = excluded_languages(dictionary=value_or_dict, exclude_list=exclude_list)

            else:
                new_dictionary[key] = value_or_dict

    return new_dictionary


def cog_list() -> list:
    path = Path(__file__).parent
    return [f"cogs.{command_name.stem}" for command_name in Path(path, "cogs").absolute().glob("*.py")]


def cog_description(file_path: Path) -> Dotted:
    path = Path(file_path)
    return Dotted(open_json(Path(path.parent, COMMANDS_PATH, path.stem.lower(), TEXT_PATH, DESCRIPTION_JSON)))


def cog_response(file_path: Path, json_name: str = None) -> Dotted:
    json_name = json_name if json_name else RESPONSE_JSON
    path = Path(file_path)
    invalid_translation = exclude.__getattribute__(path.parent.name)
    response_dictionary = open_json(file_path=Path(path.parent, TEXT_PATH, json_name))

    if invalid_translation:
        return Dotted(excluded_languages(dictionary=response_dictionary, exclude_list=invalid_translation))

    else:
        return Dotted(response_dictionary)


def list_to_path(file_path: list) -> Path:
    absolute = Path(__file__).parent
    return Path(absolute, *file_path)


def list_to_response(file_path: list) -> Dotted:
    absolute = Path(__file__).parent
    return Dotted(open_json(Path(absolute, *file_path)))
