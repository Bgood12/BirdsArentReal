from src.db.db_utils import *
import hashlib
import datetime

def createUser(username, password):
    """
    Cretaes a new user and adds them to the database
    :param username: The username of the new user
    :param password: The user's password
    :return:
    """
    hash = hashlib.sha256(password.encode('utf-8')).hexdigest() # The encoded password
    creation_date = datetime.datetime.now() # Also the last_access_date because it's a new account
    create_sql = "INSERT INTO users (username, password, creation_date, last_access_date)" \
                 "VALUES (%s, %s, %s, %s)"
    exec_commit(create_sql, [username, hash, creation_date, creation_date])


