"""
    merge processed files so that the structure of the original SQUADv2.0 is obtained
"""
from utils import *
import os


dir_path =  "/home/sebastian/SideProject/QA/German_SQUADv2.0/data/squad_data/output/processed/"
save_path = "/home/sebastian/SideProject/QA/German_SQUADv2.0/data/squad_data/output/processed/train_v2_german.json"
template = {
    "version": "v2.0",
    "data": []
}

for file_name in os.listdir(dir_path):
    abs_file_path = os.path.join(dir_path, file_name)
    if not os.path.isdir(abs_file_path):
        data = load_json(abs_file_path)
        template['data'].extend(data['data'])
        dump_json(template, save_path)
