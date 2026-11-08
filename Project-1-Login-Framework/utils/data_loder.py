import json

def data_loader(data):
    with open(data, "r", encoding="utf-8") as data_file:
        data = data_file.read()
        return json.loads(data)

