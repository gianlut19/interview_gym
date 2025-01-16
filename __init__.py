import os
import json

PATH = "credentials.json"
if os.path.exists(PATH):
    with open(PATH, "r") as f:  
        os.environ["HF_ACCESS_TOKEN"] = json.load(f)["HUGGING_TOKEN"]