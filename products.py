from storage import read_json, write_json, PRODUCTS_FILE

def add_product(product):
    """Adds a new product"""
    products = read_json(PRODUCTS_FILE)
    products.append(product)
    write_json(PRODUCTS_FILE, products)
    return product

def get_products():
    """Returns all products"""
    return read_json(PRODUCTS_FILE)
