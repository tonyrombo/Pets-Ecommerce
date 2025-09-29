from flask import Flask, request, jsonify
from users import register_user, get_users, login_user
from products import add_product, get_products, update_product, delete_product
from sales import add_sale, get_sales, delete_sale

app = Flask(__name__)

# --- User Endpoints ---
@app.route("/users", methods=["GET"])
def list_users():
    return jsonify(get_users())

@app.route("/users", methods=["POST"])
def create_user():
    user = request.json
    return jsonify(register_user(user)), 201

@app.route("/login", methods=["POST"])
def login():
    credentials = request.json
    return jsonify(login_user(credentials))

# --- Product Endpoints ---
@app.route("/products", methods=["GET"])
def list_products():
    return jsonify(get_products())

@app.route("/products", methods=["POST"])
def create_product():
    product = request.json
    return jsonify(add_product(product)), 201

@app.route("/products/<product_id>", methods=["PUT"])
def update_product_route(product_id):
    new_data = request.json
    return jsonify(update_product(product_id, new_data))

@app.route("/products/<product_id>", methods=["DELETE"])
def delete_product_route(product_id):
    return jsonify(delete_product(product_id))

# --- Sales Endpoints ---
@app.route("/sales", methods=["GET"])
def list_sales():
    return jsonify(get_sales())

@app.route("/sales", methods=["POST"])
def create_sale():
    sale = request.json
    return jsonify(add_sale(sale)), 201

@app.route("/sales/<sale_id>", methods=["DELETE"])
def delete_sale_route(sale_id):
    return jsonify(delete_sale(sale_id))

if __name__ == "__main__":
    app.run(debug=True, port=5001)