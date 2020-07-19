from utils import load_json
import tqdm


file_path = "/home/sebastian/SideProject/QA/German_SQUADv2.0/data/squad_data/output/processed/merged/clean/train_v2_german.json"

data = load_json(file_path)

#iterate through squad data and translate 
for ct, item in enumerate(data['data']):
    print(ct)
    for key in item.keys(): #keys are "title" and "paragraphs"
        if key == 'title':
            print(item[key])
        else:                   #paragraphs
            for c, para in enumerate(tqdm.tqdm(item[key])): #TODO:remove enumerate, only for testing
                if c <= 1: #TODO:remove enumerate, only for testing
                    print("----------------------")
                    for k in para.keys():
                        
                        if k == 'qas':  # questions and answer part
                            for qas in para[k]:
                                for k2 in qas.keys():  # iterate over plausible_answers (if existent), question, id, answers
                                    if k2 == 'plausible_answers':
                                        print("plausible_answer")
                                        for pa in qas[k2]:
                                            print(">",pa['text'])
                                    if k2 == 'answers':
                                        print('answer')
                                        for a in qas[k2]:
                                            
                                            print(">>",a['text'])
                                            print(">>start", a['answer_start'])

   
                                    if k2 == 'question': 
                                        print("question")
                                        print(qas[k2])           
                        else:       
                            print("context") # context       
                            print(para[k])
                else:
                    break #TODO:remove enumerate, only for testing