# 🐾 PetShop API

This project is a simple API for a pet e-commerce.  
It allows managing **users, products, and sales** using Flask and JSON files as storage.

---

## 📌 Requirements

Before running the application, make sure you have installed:

- [Python 3.9+](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/)

Install Flask with:

```bash
pip install flask
```

## 🌐 Endpoints

### Users

- **POST** `/users` → create a new user  

Request body:

```json
{
  "username": "john",
  "password": "1234",
  "role": "admin"
}
```

- **GET** `/users` → list all users

### Products

- **POST** `/products` → create a new product

Request body:

```json
{
  "name": "Dog Food",
  "price": 15.99,
  "stock": 20
}
```

- **GET** `/products` → list all products

### Sales

- **POST** `/sales` → create a sale

Request body:

```json
{
  "user": "john",
  "items": [
    { "product": "Dog Food", "quantity": 2 }
  ],
  "total": 31.98
}
```

- **GET** `/sales` → list all sales

### 🧪 Testing with Postman

1. Open Postman.

2. Create a request for POST http://127.0.0.1:5001/users.

3. In the Body tab, select raw → JSON and paste:
```json
{
  "username": "john",
  "password": "1234",
  "role": "admin"
}
```

4. Click Send.

5. Repeat similar steps for /products and /sales.

6. After making POST requests, check the generated JSON files (users.json, products.json, sales.json) to confirm the data was stored.

