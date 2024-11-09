from absolute_path import list_to_response

JSON_JSON = list_to_response(file_path=["cogs", "commands", "tarot", "text", "response.json"])


for number in range(40, 46):
    key_positive = JSON_JSON["cards"][f"{number}"]["description"]["1"]["keywords"].keys()
    key_negative = JSON_JSON["cards"][f"{number}"]["description"]["-1"]["keywords"]

    for k in key_positive:
        print(f"{k}: {JSON_JSON["cards"][f"{number}"]["description"]["1"]["text"][k]}")

    print()
    for k in key_positive:
        print(f"{k}: {JSON_JSON["cards"][f"{number}"]["description"]["-1"]["text"][k]}")
    print()