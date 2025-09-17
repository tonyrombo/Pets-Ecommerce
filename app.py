from flask import Flask, request, jsonify
from users import register_user, get_users
from products import add_product, get_products
from sales import add_sale, get_sales

app = Flask(__name__)

# --- Endpoints for Users ---
@app.route("/users", methods=["GET"])
def list_users():
    return jsonify(get_users())

@app.route("/users", methods=["POST"])
def create_user():
    user = request.json
    return jsonify(register_user(user)), 201

# --- Endpoints for Products ---
@app.route("/products", methods=["GET"])
def list_products():
    return jsonify(get_products())

@app.route("/products", methods=["POST"])
def create_product():
    product = request.json
    return jsonify(add_product(product)), 201

# --- Endpoints for Sales ---
@app.route("/sales", methods=["GET"])
def list_sales():
    return jsonify(get_sales())

@app.route("/sales", methods=["POST"])
def create_sale():
    sale = request.json
    return jsonify(add_sale(sale)), 201

if __name__ == "__main__":
    app.run(debug=True, port=5001)
