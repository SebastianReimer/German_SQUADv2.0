'''
 texts in squad were translated into German but answer spans (or starts)
 remained the same (corrsponding to English texts)
 The start of the answers are adjusted to to German text. 
 Answers which cannot be found in the German text will be dropped
'''

from utils import *
import re

file_path = "/home/sebastian/SideProject/QA/German_SQUADv2.0/data/squad_data/output/squad_dev_german.json"

data = load_json(file_path)


answers: [{"text": "10. und 11. Jahrhundert", "answer_start": 94}]
text = "Die Normannen (Normanisch: Nourmands; Franz\u00f6sisch: Normands; Lateinisch: Normanni) waren das Volk, das im 10. und 11. Jahrhundert der Normandie, einer Region in Frankreich, ihren Namen gab. Sie stammten von Norse (\"Norman\" kommt von \"Norseman\") R\u00e4ubern und Piraten aus D\u00e4nemark, Island und Norwegen, die unter ihrem Anf\u00fchrer Rollo dem K\u00f6nig Karl III. W\u00e4hrend es in den letzten Jahren zu einem gro\u00dfen Aufschwung gekommen ist, hat es in den letzten Jahren zu einem gro\u00dfen Aufschwung gekommen. Durch Generationen der Assimilierung und Vermischung mit den einheimischen Franken und r\u00f6misch-gallischen Bev\u00f6lkerungen f\u00fcgten sich ihre Nachkommen allm\u00e4hlich mit den karolingischen Kulturen des Westens der Francia zusammen. Die kulturelle und ethnische Identit\u00e4t der Normannen entstand zun\u00e4chst in der ersten H\u00e4lfte des 10. Jahrhunderts und entwickelte sich in den folgenden Jahrhunderten weiter."
#print(text[0:200])

answers_en: [{"text": "10th and 11th centuries", "answer_start": 94}]
text_en = "The Normans (Norman: Nourmands; French: Normands; Latin: Normanni) were the people who in the 10th and 11th centuries gave their name to Normandy, a region in France. They were descended from Norse (\"Norman\" comes from \"Norseman\") raiders and pirates from Denmark, Iceland and Norway who, under their leader Rollo, agreed to swear fealty to King Charles III of West Francia. Through generations of assimilation and mixing with the native Frankish and Roman-Gaulish populations, their descendants would gradually merge with the Carolingian-based cultures of West Francia. The distinct cultural and ethnic identity of the Normans emerged initially in the first half of the 10th century, and it continued to evolve over the succeeding centuries."
#print(text_en[94])

paragraph = data['data'][0]['paragraphs'][0]


squad_small = {
    "version":"v2.0",
    "data": [
        {
            "title": "Normans",
            "paragraphs": paragraph
        }
    ]
}
#print(data['data'][0]['paragraphs'][0]['qas'][1])



char_space = 100 #search 100 chars before and after answer_start in English version

for ct, item in enumerate(squad_small['data']): #TODO change dict
    print(f"Paragraph no. {ct}")
    for key in item.keys(): #keys are "title" and "paragraphs"
        if key == 'title':
            print(item[key]) 
        else:       
            context = item[key]['context']
            len_con = len(context) -1
            print(context)
            
            #iterate over questions and answers
            for qas in item[key]['qas']:
                print("-----qas-------")
                print(qas.keys())
                list2keep = []
                for ctr, answer in enumerate(qas['answers']):
                    #print("--------------------")
                    #print(f">>>answer before:")
                    #print(answer)
                    #define start and end string
                    if answer['answer_start'] < 100:
                        tmp_start = 0
                    else:
                        tmp_start = answer['answer_start'] - 100
                    if answer['answer_start'] + 100 > len_con:
                        tmp_end = len_con
                    else:
                        tmp_end = answer['answer_start'] + 100
                    
                    substring = context[tmp_start:tmp_end] #extract potentially relevant substring
                    
                    match = re.search(answer['text'], substring) #check if substring contains answer
                    #print(match)
                    if match: #context contains anwer
                        tmp_start_substring = substring.find(answer['text'])
                        #print(tmp_start_substring)

                        if tmp_start_substring != -1: # in case answer is not found
                            answer_start = tmp_start + tmp_start_substring    # adapt start of answer from substring to context
                            answer['answer_start'] = answer_start
                            list2keep.append(answer)
                            #print(answer['text'])
                            #print(answer['answer_start'])
                            #print(context[answer_start:answer_start+35])
                       # else: #context does not contain answer
                       #     print(f">>>answer deleted 1:")
                       #     print(answer)
                       #     #del qas['answers'][ctr]
                       #     list2delete.append(ctr)

                        #TODO for plausible answers
                        #print(f">>>answer after:")
                        #print(answer)

                    #else: #context does not contain answer
                        #print(f">>>answer deleted 2:")
                        #print(answer)
                        #list2delete.append(ctr)

                #only keep answer which answers appear in context
                qas['answers'] = list2keep

                list2keep = []
########################################hier weiter machen##########################################
                if qas['plausible_answers']:

                    for ctr, answer in enumerate(qas['plausible_answers']):
                        print("--------------------")
                        print(f">>>answer before:")
                        print(answer)
                        #define start and end string
                        if answer['answer_start'] < 100:
                            tmp_start = 0
                        else:
                            tmp_start = answer['answer_start'] - 100
                        if answer['answer_start'] + 100 > len_con:
                            tmp_end = len_con
                        else:
                            tmp_end = answer['answer_start'] + 100
                        
                        substring = context[tmp_start:tmp_end] #extract potentially relevant substring
                        
                        match = re.search(answer['text'], substring) #check if substring contains answer
                        #print(match)
                        if match: #context contains anwer
                            tmp_start_substring = substring.find(answer['text'])
                            #print(tmp_start_substring)

                            if tmp_start_substring != -1: # in case answer is not found
                                answer_start = tmp_start + tmp_start_substring    # adapt start of answer from substring to context
                                answer['answer_start'] = answer_start
                                list2keep.append(answer)
                        print(f">>>answer after:")
                        print(answer)


                    #only keep answer which answers appear in context
                    qas['plausible_answers'] = list2keep
########################################hier weiter machen##########################################

print(squad_small)                    

