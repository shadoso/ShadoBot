import os
import json


class Dotted(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


def root_path(where: list):
    """
    It only works if this file is in the root directory
    :param where: A list of directories
    :return: Absolute Path
    """
    first_element = 0
    abs_path = os.path.dirname(os.path.abspath(__file__))
    where.insert(first_element, abs_path)

    return "/".join(where)


def filenames(where: list):
    return os.listdir(root_path(where=where))


def json_text(where: list, commands: list):
    all_cmd = {}

    with open(file=root_path(where=where)) as file:
        file = json.load(file)

    for item in commands:
        all_cmd[item] = file[item]

    all_cmd = Dotted(all_cmd)
    return all_cmd


if __name__ == "__main__":
    url = ["config", ".env"]
    testing = root_path(url)
    print(testing)
    many_files = ["app", "old_not_in_use", "features"]
    testing1 = filenames(many_files)
    print(testing1)
    js = ["app", "languages", "info.json"]
    rs = ["language"]
    testing2 = json_text(where=js, commands=rs)
    print(testing2.language)
