from storage import read_json, write_json, USERS_FILE, generate_id

def register_user(user):
    """Adds new user with validation"""
    if "username" not in user or "password" not in user or "role" not in user:
        return {"error": "username, password and role are required"}

    users = read_json(USERS_FILE)

    # Validate unique username
    if any(u["username"] == user["username"] for u in users):
        return {"error": "Username already exists"}

    user["id"] = generate_id()
    users.append(user)
    write_json(USERS_FILE, users)
    return user

def get_users():
    """Returns all the users"""
    return read_json(USERS_FILE)

def login_user(credentials):
    """Basic login validation"""
    users = read_json(USERS_FILE)
    for u in users:
        if u["username"] == credentials.get("username") and u["password"] == credentials.get("password"):
            return {"message": "Login successful", "user": u}
    return {"error": "Invalid username or password"}