from absolute_path import list_to_response, list_to_path
from absolute_path import save_json

JSON_JSON = list_to_response(file_path=["cogs", "commands", "tarot", "text", "response.json"])
name_file = list_to_path(["tarot_name.txt"])
text_file = list_to_path(["tarot_keywords.txt"])

card = 0
times = 0
key_type = 1
tags = ["es_ES", "fr", "pt_BR"]

with open(name_file, "r") as name_text:
    for line in name_text:
        splited = line.strip().split(":")

        if len(splited) != 2:
            continue

        if splited[0] in tags:
            times += 1
            # print(f"Processing {splited[0]}: {splited[1]}")
            # print(f"Before update: {JSON_JSON['cards'][f'{card}']['name']}")
            numer_text = f"{JSON_JSON["cards"][f"{card}"]["name"]["default"][:2]} "
            JSON_JSON["cards"][f"{card}"]["name"][splited[0]] = numer_text + splited[1].strip()

            # print(f"After update: {JSON_JSON['cards'][f'{card}']['name']}")
            # print(f"Card index: {card}")

            if times % 3 == 0:
                times = 0
                card += 1
        # print()

times = 0
card = 0

with open(text_file, "r") as keywords_:
    for line in keywords_:
        splited = line.strip().split(":")

        if len(splited) != 2:
            continue

        if splited[0] in tags:
            times += 1

            JSON_JSON["cards"][f"{card}"]["description"][str(key_type)]["keywords"][splited[0]] = splited[1].strip()

        if times % 3 == 0:
            key_type *= -1

            if times % 6 == 0 and times > 0:
                card += 1
                times = 0

json_path_name = list_to_path(["cogs", "commands", "tarot", "text", "response.json"])

save_json(file_path=json_path_name, file=JSON_JSON)