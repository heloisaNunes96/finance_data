import json


def save_json(data, file_path):
    #salva o arquivo no disco:
    
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)