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
    if not isUniqueUsername(username): # If the username is not unique
        print("Proposed username isn't unique")
        return # Do not add the entry

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

def updateUsername(old_username, new_username):
    """
    Updates the username of a user entry
    :param old_username: The old username, for identifying the entry
    :param new_username: The new username
    :return:
    """
    if new_username: # If there is a new username
        if not isUniqueUsername(new_username): # If the username is not unique
            print("Proposed username isn't unique")
            return # Do not update the username
    else: # If new_username hasn't been specified
        new_username = old_username

    update_sql = "UPDATE users SET username = %s WHERE username = %s"
    exec_commit(update_sql, [new_username, old_username])

def updatePassword(username, password):
    """
    Updates the password of a user's user account
    :param username: The username identifying the account
    :param password: The new password
    :return:
    """
    hash = hashlib.sha256(password.encode('utf-8')).hexdigest()  # The encoded password
    update_sql = "UPDATE users SET password = %s WHERE username = %s"
    exec_commit(update_sql, [hash, username])

def updateLastAccess(username, last_access):
    """
    Updates the user's last access date
    :param username: The username identifying the account
    :param last_access: The last access date
    :return:
    """
    update_sql = "UPDATE users SET last_access_date = %s WHERE username = %s"
    exec_commit(update_sql, [last_access, username])

def listUsers():
    """
    Gets all usernames from the users table
    :return: A tuple containing all usernames
    """
    exec_get_all('SELECT username FROM users')

def isUniqueUsername(username) -> bool:
    """
    Determines if the passed username is unique
    :param username: The username being passed in
    :return: True if username is unique false otherwise
    """
    users = listUsers() # Get a list of all the users
    for user in users[0]: # For each tuple in users
        if user[0] == username:
            return False # The username found a match so it is not unique
    return True # No match was found
