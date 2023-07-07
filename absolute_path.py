from pathlib import Path
from json import load
from languages.excluded_languages import exclude

TEXT = "text"


class Dotted(dict):
    __getattr__ = dict.__getitem__


def open_json(file_path: Path) -> dict:
    with open(file=file_path) as json_file:
        dictionary = load(json_file)

    return dictionary


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
    return Dotted(open_json(Path(path.parent, "commands", path.stem.lower(), TEXT, "description.json")))


def cog_response(file_path: Path) -> Dotted:
    path = Path(file_path)
    invalid_translation = exclude.__getattribute__(path.parent.name)
    response_dictionary = open_json(file_path=Path(path.parent, TEXT, "response.json"))

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
