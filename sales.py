from storage import read_json, write_json, SALES_FILE, generate_id

def add_sale(sale):
    """Adds new sale with validation"""
    if "user" not in sale or "items" not in sale or "total" not in sale:
        return {"error": "user, items and total are required"}

    sales = read_json(SALES_FILE)
    sale["id"] = generate_id()
    sales.append(sale)
    write_json(SALES_FILE, sales)
    return sale

def get_sales():
    """Returns all sales"""
    return read_json(SALES_FILE)

def delete_sale(sale_id):
    """Delete a sale by id"""
    sales = read_json(SALES_FILE)
    new_sales = [s for s in sales if s["id"] != sale_id]
    if len(new_sales) == len(sales):
        return {"error": "Sale not found"}
    write_json(SALES_FILE, new_sales)
    return {"message": "Sale deleted"}