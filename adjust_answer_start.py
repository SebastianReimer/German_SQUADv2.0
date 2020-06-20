'''
 texts in squad were translated into German but answer spans (or starts)
 remained the same (corrsponding to English texts)
 The start of the answers are adjusted to to German text. 
 Answers which cannot be found in the German text will be dropped
'''

from utils import *

file_path = "/home/sebastian/SideProject/QA/German_SQUADv2.0/data/squad_data/output/squad_dev_german.json"

data = load_json(file_path)


answers: [{"text": "10. und 11. Jahrhundert", "answer_start": 94}]
text = "Die Normannen (Normanisch: Nourmands; Franz\u00f6sisch: Normands; Lateinisch: Normanni) waren das Volk, das im 10. und 11. Jahrhundert der Normandie, einer Region in Frankreich, ihren Namen gab. Sie stammten von Norse (\"Norman\" kommt von \"Norseman\") R\u00e4ubern und Piraten aus D\u00e4nemark, Island und Norwegen, die unter ihrem Anf\u00fchrer Rollo dem K\u00f6nig Karl III. W\u00e4hrend es in den letzten Jahren zu einem gro\u00dfen Aufschwung gekommen ist, hat es in den letzten Jahren zu einem gro\u00dfen Aufschwung gekommen. Durch Generationen der Assimilierung und Vermischung mit den einheimischen Franken und r\u00f6misch-gallischen Bev\u00f6lkerungen f\u00fcgten sich ihre Nachkommen allm\u00e4hlich mit den karolingischen Kulturen des Westens der Francia zusammen. Die kulturelle und ethnische Identit\u00e4t der Normannen entstand zun\u00e4chst in der ersten H\u00e4lfte des 10. Jahrhunderts und entwickelte sich in den folgenden Jahrhunderten weiter."
print(text[90:120])

answers_en: [{"text": "10th and 11th centuries", "answer_start": 94}]
text_en = "The Normans (Norman: Nourmands; French: Normands; Latin: Normanni) were the people who in the 10th and 11th centuries gave their name to Normandy, a region in France. They were descended from Norse (\"Norman\" comes from \"Norseman\") raiders and pirates from Denmark, Iceland and Norway who, under their leader Rollo, agreed to swear fealty to King Charles III of West Francia. Through generations of assimilation and mixing with the native Frankish and Roman-Gaulish populations, their descendants would gradually merge with the Carolingian-based cultures of West Francia. The distinct cultural and ethnic identity of the Normans emerged initially in the first half of the 10th century, and it continued to evolve over the succeeding centuries."
print(text_en[94])