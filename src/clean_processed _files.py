"""
    remove empty list of answers and plausible answers
"""

from utils import *
import os
import tqdm

file_path = "/home/sebastian/SideProject/QA/German_SQUADv2.0/data/squad_data/output/processed/merged/merged_train_v2_german.json"
save_path =  "/home/sebastian/SideProject/QA/German_SQUADv2.0/data/squad_data/output/processed/merged/clean/train_v2_german.json"

data = load_json(file_path)



template = {
    "version": "v2.0",
    "data": [data['data'][0]] # []
}
#delete qas that contain no answers
for ct, item in enumerate(data['data']): #TODO change to data
            print(f"Paragraph no. {ct}")
            for key in item.keys(): #keys are "title" and "paragraphs"
                if key == 'title':
                    print(item[key]) 
                else: 
                    for para in tqdm.tqdm(item[key]):

                        
                        qas2keep = []
                        #print("----------------------------------------")
                        for qas in para['qas']: #iterate over qas
                            if qas['answers']: # check if there anwers
                                #print(qas)
                                #print(qas['answers'])
                                
                                qas2keep.append(qas)
                        #print(qas2keep)
                        if qas2keep: # only keep non-empty qas
                            para['qas'] = qas2keep
                        else: # if it is empty, mark it so that it can be deleted later
                            para['qas'] = ["deleteme"]  
         
                        #print(para['qas'][0]['answers'])
                            #print(qas)



# delete empty paragraphs that contain to questions
for ct, item in enumerate(data['data']): #TODO change to data
            print(f"Paragraph no. {ct}")
            for key in item.keys(): #keys are "title" and "paragraphs"
                if key == 'title':
                    print(item[key]) 
                else: 
                    para2keep = []
                    for para in tqdm.tqdm(item[key]):
                        #print("----------------------------------------")
                        if not (para['qas'][0] == "deleteme"):
                            para2keep.append(para)

                    item[key] = para2keep
                    print(len(para2keep))
dump_json(data, save_path)