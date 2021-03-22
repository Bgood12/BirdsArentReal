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

def getUserByUsername(username):
    """
    Gets a user by their username
    :param username: The username to look up
    :return: A tuple containing the user's data entry
    """
    return exec_get_one('SELECT * FROM users WHERE username = %s', [username])

def deleteUserByUsername(username):
    """
    Deletes a user profile by their username
    :param username: The username identifying the user to delete
    :return:
    """
    exec_commit('DELETE FROM users WHERE username = %s', [username])

def updateUser(username, password, last_access, new_username = ''):
    """
    Updates a user entry
    :param username: The username to identify the use entry with
    :param password: The user's new password
    :param last_access: The last time the user account has been accessed
    :param new_username: The user's new username (optional)
    :return:
    """
    if not new_username: # If new_username hasn't been specified
        new_username = username

    hash = hashlib.sha256(password.encode('utf-8')).hexdigest()  # The encoded password
    update_sql = "UPDATE users SET username = %s, password = %s, last_access_date = %s WHERE username = %s"
    exec_commit(update_sql, [new_username, hash, last_access, username])
