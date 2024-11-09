import os

IGNORE_DIRS = ["venv", ".git", ".idea", "__pycache__", ".gitignore", "creatures",
               "tree.py", "templates", "features", "embed_recovery", "creative_zone",
               "errors", "not_implemented", "old_not_in_use"]  # adicione quantos diretórios quiser aqui


def print_directory_tree(startpath, prefix='', print_files=False):
    if not prefix:
        print(startpath)
    entries = sorted(os.scandir(startpath), key=lambda e: e.name.lower())
    entries = [entry for entry in entries if entry.is_dir(follow_symlinks=False) or print_files]

    for i, entry in enumerate(entries):
        if entry.name in IGNORE_DIRS:
            continue
        if i == len(entries) - 1:
            new_prefix = prefix + '└── '
            indent = '    '
        else:
            new_prefix = prefix + '├── '
            indent = '|   '

        if entry.is_dir(follow_symlinks=False):
            entry_name = entry.name + '/'
            print(new_prefix + entry_name)
            print_directory_tree(entry.path, prefix=prefix + indent, print_files=print_files)
        elif print_files:
            print(new_prefix + entry.name)


print_directory_tree('/home/bismuto/PycharmProjects/ShadoBot', print_files=True)