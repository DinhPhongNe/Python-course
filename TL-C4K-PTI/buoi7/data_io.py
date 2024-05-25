import json

def load_json_data():
    list_data = list()
    with open("json.txt", "r") as json_in:
        json_data = json.load(json_in)
    list_data.extend(json_data)
    return list_data

    
def write_json_data(json_data):
    with open("json.txt", "w") as json_out:
        json.dump(json_data, json_out, indent=4)