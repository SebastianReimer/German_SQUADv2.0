import os
import json
import tqdm

from nltk.tokenize import sent_tokenize
from transformers import pipeline
import re


def translate(translator, text_en):
    """
    Translates English texts into German

    :translator: instance of a pipeline
    :text_en: English text which should be translated
    :return text_de:  Translated text in German
    """    

    #remove trailing white space on right side
    text_en = text_en.rstrip()
 


    # in case there is no fullstop at the end (e.g. answers)
    # add fullstop, so a correct translation will be made
    # remove fullstop after translation
    match = re.search(r'\.$', text_en)# contains None if pattern was not found

    if not match: #string does not contains full stop at the end
        text_en = text_en + "." 

    #translate sentence-wise
    text_split = sent_tokenize(text_en)

    translated = []
    for sent in text_split: 
        sent_de = translator(sent)
        sent_de = sent_de[0]['translation_text']  
        translated.append(sent_de)

    #concat single sentences into one text
    text_de = ""
    text_de = " ".join(translated)

    if not match: #remove full stop
        text_de = re.sub(r'\.$', '', text_de)
    return text_de

def load_json(file_path):
    data = {}
    with open(file_path) as f:
        data = json.load(f)
    return data

def dump_json(dict2save, path):
    with open(path, 'w') as f:
        json.dump(dict2save, f)  


# instantiate the translator
translator = pipeline(task="translation_en_to_de")


# read original SQUAD
file_path = "/home/sebastian/SideProject/QA/German_SQUADv2.0/data/squad_data/dev-v2.0.json"

data = load_json(file_path)


print(len(data['data']))
#iterate over whole data and identify texts which should be translated
for ct, item in enumerate(data['data']):
    print(f"Paragraph no. {ct}")
    for key in item.keys(): #keys are "title" and "paragraphs"
        if key == 'title':
            print(item[key]) 
        else:                   #paragraphs
            for c, para in enumerate(tqdm.tqdm(item[key])): #TODO:remove enumerate, only for testing
                #if c <= 1: #TODO:remove enumerate, only for testing
                    for k in para.keys():
                        if k == 'qas':  # questions and answer part
                            for qas in para[k]:
                                for k2 in qas.keys():  # iterate over plausible_answers (if existent), question, id, answers
                                    if k2 == 'plausible_answers':
                                        for pa in qas[k2]:
                                            pa['text'] = translate(translator,pa['text']) 
                                            #print(pa['text'])
                                            #pa['start_answer'] #TODO adjust answer_start to german
                                    if k2 == 'answers':
                                        for a in qas[k2]:
                                            a['text'] = translate(translator, a['text']) 
                                            #print(a['text'])
                                            #a['start_answer'] #TODO adjust answer_start to german
                                    if k2 == 'question': 
                                        #print("question")
                                        qas[k2] = translate(translator, qas[k2])  
                                        #print(qas[k2])           
                        else:       
                            #print("context") # context       
                            para[k] = translate(translator, para[k])    
                            #print(para[k])
                #else:
                #    break #TODO:remove enumerate, only for testing

# dump the translated data        
dump_json(data, "/home/sebastian/SideProject/QA/German_SQUADv2.0/data/squad_data/squad_train_german.json")
