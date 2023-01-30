import json


def init(path_file: str):
    with open(path_file, 'r', encoding='utf-8') as data:
        school = json.load(data)
    return school