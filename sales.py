from storage import read_json, write_json, SALES_FILE

def add_sale(sale):
    """Adds new sale"""
    sales = read_json(SALES_FILE)
    sales.append(sale)
    write_json(SALES_FILE, sales)
    return sale

def get_sales():
    """Returns all sales"""
    return read_json(SALES_FILE)
