import os
import json

FIRST_ELEMENT = 0


def arquive(where: list):
    """
    It only works if this file is in the root directory
    :param where: A list of directories
    :return: Absolute Path
    """
    root_path = os.path.dirname(os.path.abspath(__file__))
    where.insert(FIRST_ELEMENT, root_path)

    return "/".join(where)


def filenames(where: list):
    return os.listdir(arquive(where=where))


def json_file(where: list, commands: list):
    command = []

    with open(file=arquive(where=where)) as file:
        dic = json.load(file)

    for item in commands:
        command.append(dic[item])

    return command


if __name__ == "__main__":
    url = ["main", ".env"]
    testing = arquive(url)
    print(testing)
    many_files = ["app", "old_not_in_use", "features"]
    testing1 = filenames(many_files)
    print(testing1)
    js = ["app", "languages", "info.json"]
    rs = ["language"]
    testing2 = json_file(where=js, commands=rs)[0]
    print(testing2["names"])
