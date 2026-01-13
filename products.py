from storage import read_json, write_json, PRODUCTS_FILE, generate_id

def add_product(product):
    """Adds a new product with validation"""
    if "name" not in product or "price" not in product or "stock" not in product:
        return {"error": "name, price and stock are required"}

    products = read_json(PRODUCTS_FILE)
    product["id"] = generate_id()
    products.append(product)
    write_json(PRODUCTS_FILE, products)
    return product

def get_products():
    """Returns all products"""
    return read_json(PRODUCTS_FILE)

def update_product(product_id, new_data):
    """Update an existing product"""
    products = read_json(PRODUCTS_FILE)
    for p in products:
        if p["id"] == product_id:
            p.update(new_data)
            write_json(PRODUCTS_FILE, products)
            return p
    return {"error": "Product not found"}

def delete_product(product_id):
    """Delete a product by id"""
    products = read_json(PRODUCTS_FILE)
    new_products = [p for p in products if p["id"] != product_id]
    if len(new_products) == len(products):
        return {"error": "Product not found"}
    write_json(PRODUCTS_FILE, new_products)
    return {"message": "Product deleted"}