import json
import os
import uuid

# JSON files to simulate database
USERS_FILE = "data/users.json"
PRODUCTS_FILE = "data/products.json"
SALES_FILE = "data/sales.json"

def read_json(filepath):
    """Returns the content of the JSON file or an empty list if no file or invalid JSON"""
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []  # corrupted file → reset to empty list

def write_json(filepath, data):
    """Writes into the JSON file"""
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)

def generate_id():
    """Generate a unique ID"""
    return str(uuid.uuid4())
