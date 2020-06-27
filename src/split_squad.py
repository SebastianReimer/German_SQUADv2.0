'''
Split squad dataset into smaller chunks
'''

import os
import json
import tqdm
from utils import *

# read original SQUAD
file_path = "/home/sebastian/SideProject/QA/German_SQUADv2.0/data/squad_data/train-v2.0.json"

data = load_json(file_path)

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
    