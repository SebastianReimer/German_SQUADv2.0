import requests
import json
import tqdm

url = "http://localhost:5000/translate"

text_en= "The Norman dynasty had a major political, cultural and military impact on medieval Europe and even the Near East. The Normans were famed for their martial spirit and eventually for their Christian piety, becoming exponents of the Catholic orthodoxy into which they assimilated. They adopted the Gallo-Romance language of the Frankish land they settled, their dialect becoming known as Norman, Normaund or Norman French, an important literary language. The Duchy of Normandy, which they formed by treaty with the French crown, was a great fief of medieval France, and under Richard I of Normandy was forged into a cohesive and formidable principality in feudal tenure. The Normans are noted both for their culture, such as their unique Romanesque architecture and musical traditions, and for their significant military accomplishments and innovations. Norman adventurers founded the Kingdom of Sicily under Roger II after conquering southern Italy on the Saracens and Byzantines, and an expedition on behalf of their duke, William the Conqueror, led to the Norman conquest of England at the Battle of Hastings in 1066. Norman cultural and military influence spread from these new European centres to the Crusader states of the Near East, where their prince Bohemond I founded the Principality of Antioch in the Levant, to Scotland and Wales in Great Britain, to Ireland, and to the coasts of north Africa and the Canary Islands."

def translate(text_en):
    """
    Translates English texts into German

    :text_en: English text
    :return text_de:  Translated text in German
    """    

    input_translator = { 
    "text": text_en,
    "source":"en",
    "target":"de"
    }

    res = requests.post(url, json=input_translator)
    text_de = res.json()['output']

    return text_de

def load_json(file_path):
    data = {}
    with open(file_path) as f:
        data = json.load(f)
    return data

def dump_json(dict2save, path):
    with open(path, 'w') as f:
        json.dump(dict2save, f)    


# read original SQUAD
file_path = "/home/sebastian/SideProject/QA/German_SQUADv2.0/data/dev-v2.0.json"

data = load_json(file_path)
#print(data['data'][0].keys())

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



#print(squad_small['data'][0]['paragraphs'])
#print(paragraph[0]['context'])
#iterate over whole data and identify texts which should be translated
for item in squad_small['data']:
    for key in item.keys(): #keys are "title" and "paragraphs"
        if key == 'title':
            print(item[key])
        else:                   #paragraphs
            for para in tqdm.tqdm(item[key]):
                for k in para.keys():
                    if k == 'qas':  # questions and answer part
                        for qas in para[k]:
                            for k2 in qas.keys():  # iterate over plausible_answers (if existent), question, id, answers
                                if k2 == 'plausible_answers':
                                    for pa in qas[k2]:
                                        pa['text'] = -1 #translate(pa['text']) #TODO: translate
                                        #pa['start_answer'] #TODO adjust answer_start to german
                                        #print(pa)
                                if k2 == 'answers':
                                    for a in qas[k2]:
                                        a['text'] = -1#translate(a['text']) #TODO: translate
                                        #a['start_answer'] #TODO adjust answer_start to german
                                        #print(a)
                                if k2 == 'question':   
                                    qas[k2] = -1#translate(qas[k2])  #TODO: translate           
                    else:           # context
                        para[k] = -1#translate(para[k]) #TODO: translate     
                        #print(para[k])
            
dump_json(squad_small, "/home/sebastian/SideProject/QA/German_SQUADv2.0/data/squad_small_german.json")

