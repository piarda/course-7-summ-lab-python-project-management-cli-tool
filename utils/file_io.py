# utils/file_io.py

import json
import os

def load_data(filepath):
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
        
def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)
