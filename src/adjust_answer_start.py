'''
 texts in squad were translated into German but answer spans (or starts)
 remained the same (corrsponding to English texts)
 The start of the answers are adjusted to to German text. 
 Answers which cannot be found in the German text will be dropped
'''

from utils import *
import re
import tqdm
import os


dir_path = "/home/sebastian/SideProject/QA/German_SQUADv2.0/data/squad_data/output/"

save_dir =  "/home/sebastian/SideProject/QA/German_SQUADv2.0/data/squad_data/output/processed/"

count_answer_before = 0
count_answer_deleted = 0

count_plausanswer_before = 0
count_plausanswer_deleted = 0
for file_name in os.listdir(dir_path):
    
    abs_file_path = os.path.join(dir_path, file_name)
    if not os.path.isdir(abs_file_path):
        data = load_json(abs_file_path)



        char_space = 100 #search 100 chars before and after answer_start in English version

        for ct, item in enumerate(data['data']): #TODO change dict
            print(f"Paragraph no. {ct}")
            for key in item.keys(): #keys are "title" and "paragraphs"
                if key == 'title':
                    print(item[key]) 
                else: 

                    for para in tqdm.tqdm(item[key]):
                        #print(para.keys())
                        
                        context = para['context']
                        len_con = len(context) -1
                        #print(context)
                        
                        #iterate over questions and answers
                        for qas in para['qas']:
                            #print("-----qas-------")
                            #print(qas.keys())
                            
                            # adust answer_start in answers
                            if "answers" in qas.keys():
                                #print("xxxxxxxxxxxxxxxxxxxxx")
                                list2keep = []
                                for ctr, answer in enumerate(qas['answers']):
                                    count_answer_before += 1
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
                                    

                                    #print("> answer",answer['text'])
                                    #print(">>substring", substring)

                                    if answer['text'] in substring:
                                        match = True
                                    else:
                                        match = False
                                    #print(match)
                                    if match: #context contains anwer
                                        tmp_start_substring = substring.find(answer['text'])
                                        #print(tmp_start_substring)

                                        if tmp_start_substring != -1: # in case answer is not found
                                            answer_start = tmp_start + tmp_start_substring    # adapt start of answer from substring to context
                                            answer['answer_start'] = answer_start
                                            list2keep.append(answer)
                                            count_answer_deleted += 1
                                            #print(answer['text'])
                                            #print(answer['answer_start'])
                                            #print(context[answer_start:answer_start+35])


                                #only keep answer which answers appear in context
                                qas['answers'] = list2keep
                                
                                
                            # do it also for plausible answers
                            if "plausible_answers" in qas.keys():
                                    #print("uuuuuuuuuuuuuuuuuuuuu")
                                    list2keep = []
                                    for ctr, answer in enumerate(qas['plausible_answers']):
                                        count_plausanswer_before += 1
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
                                        
                                    # match = re.search(answer['text'], substring) #check if substring contains answer
                                        if answer['text'] in substring:
                                            match = True
                                        else:
                                            match = False
                                        #print(match)
                                        if match: #context contains anwer
                                            tmp_start_substring = substring.find(answer['text'])
                                            #print(tmp_start_substring)

                                            if tmp_start_substring != -1: # in case answer is not found
                                                answer_start = tmp_start + tmp_start_substring    # adapt start of answer from substring to context
                                                answer['answer_start'] = answer_start
                                                list2keep.append(answer)
                                                count_plausanswer_deleted += 1
                                        #print(f">>>answer after:")
                                        #print(answer)


                                    #only keep answer which answers appear in context
                                    qas['plausible_answers'] = list2keep



        save_name = "adjusted_" + file_name
        abs_save_path = os.path.join(save_dir, save_name)
        dump_json(data, abs_save_path)                 

print("> answers before:",count_answer_before)
print("> answers deleted:",count_answer_deleted)
print("> answers remaining:",count_answer_before-count_answer_deleted)
print("------------------------------------------------")
print("> plausible answers before:",count_plausanswer_before)
print("> plausible answers deleted:",count_plausanswer_deleted)
print("> plausible answers remaining:",count_plausanswer_before-count_plausanswer_deleted)