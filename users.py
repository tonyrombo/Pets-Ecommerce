from storage import read_json, write_json, USERS_FILE

def register_user(user):
    """Adds new user"""
    users = read_json(USERS_FILE)
    users.append(user)
    write_json(USERS_FILE, users)
    return user

def get_users():
    """Returns all the users"""
    return read_json(USERS_FILE)
