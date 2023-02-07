import json

def read_json(place) :
    with open(place) as json_data:
        data_dict = json.load(json_data)
    return data_dict

