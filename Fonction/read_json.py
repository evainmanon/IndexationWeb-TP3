import json

#Function which read a json file, where place is the name of the file
def read_json(place) :
    with open(place) as json_data:
        data_dict = json.load(json_data)
    return data_dict

#Function which return a part of a list
def part_list(list,number):
    if number > len(list): 
        print("Il n'y a pas autant de document dans la liste, il y en a : " + str(len(list)))
        return []
    else:
        return list[0:number]

#Function which create a json document
def create_json(liste, name_of_doc):
    with open(name_of_doc, 'w') as mon_fichier:
	    json.dump(liste, mon_fichier)