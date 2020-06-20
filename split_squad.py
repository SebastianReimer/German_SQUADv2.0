'''
Split squad dataset into smaller chunks
'''

import os
import json
import tqdm

def load_json(file_path):
    data = {}
    with open(file_path) as f:
        data = json.load(f)
    return data

def dump_json(dict2save, path):
    with open(path, 'w') as f:
        json.dump(dict2save, f)  


# read original SQUAD
file_path = "/home/sebastian/SideProject/QA/German_SQUADv2.0/data/squad_data/train-v2.0.json"

data = load_json(file_path)
#print(data['data'][0].keys())
'''
paragraph = data['data'][0]['paragraphs']
#for testing: use only one paragraph
squad_small = {
    "version":"v2.0",
    "data": [
        {
            "title": "Normans",
            "paragraphs": paragraph
        }
    ]
}
'''

print(len(data['data']))

squad_list = []
split_no = 1
#iterate over whole data and identify texts which should be translated
for ct, item in enumerate(data['data']):
    squad_list.append(item)
    #print(f"Paragraph no. {ct}")
    if (ct % 79 == 0) & (ct != 0) :
        to_dump = {
                "version":"v2.0",
                "data": squad_list
            }
        dump_json(to_dump, f"/home/sebastian/SideProject/QA/German_SQUADv2.0/data/squad_data/splitted/squad_train_{split_no}.json")
        split_no += 1
        squad_list = []
    if (ct % 441 == 0) & (ct != 0):
        to_dump = {
                "version":"v2.0",
                "data": squad_list
            }
        dump_json(to_dump, f"/home/sebastian/SideProject/QA/German_SQUADv2.0/data/squad_data/splitted/squad_train_{split_no}.json")
        split_no += 1
        squad_list = []
    

'''
    for key in item.keys(): #keys are "title" and "paragraphs"
        if key == 'title':
            print(item[key]) 
        else:                   #paragraphs
            for c, para in enumerate(tqdm.tqdm(item[key])): #TODO:remove enumerate, only for testing
                #if c <= 1: #TODO:remove enumerate, only for testing
                pass
                #else:
                #    break #TODO:remove enumerate, only for testing
'''        
#dump_json(data, "/home/sebastian/SideProject/QA/German_SQUADv2.0/data/squad_data/squad_train_german.json")
