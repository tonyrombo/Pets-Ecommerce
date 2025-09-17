import json
import os

# JSON files to simulate database
USERS_FILE = "data/users.json"
PRODUCTS_FILE = "data/products.json"
SALES_FILE = "data/sales.json"

def read_json(filepath):
    """Returns the content of the JSON file and a empty list if no file"""
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r") as f:
        return json.load(f)

def write_json(filepath, data):
    """Writes into the JSON file"""
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)
