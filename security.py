# less errors when compairing string e.g. if encoding is different
from werkzeug.security import safe_str_cmp
from models.user import UserModel  # in the same folder

# index the two most common ways to look up a password


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):  # payload is the contents of the JWT token
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
