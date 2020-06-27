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