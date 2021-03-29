from src.db.db_utils import *


def addEmail(username, email):
    """
    Adds a new email into the emails table
    :param username: The username the email belongs to
    :param email: The email being added to the db
    :return:
    """
    insert_sql = "INSERT INTO email (email, username) VALUES (%s, %s)"
    exec_commit(insert_sql, [email, username])

def deleteEmail(username, email):
    """
    Deletes an email entry from emails
    :param username: The user whose email is being removed
    :param email: The email being removed
    :return:
    """
    exec_commit('DELETE FROM email WHERE username = %s AND email = %s', [username, email])

def editEmail(username, oldEmail, newEmail):
    """
    Replaces an email address for a user
    :param username: The user whose email is being replaced
    :param oldEmail: The email to be replaced
    :param newEmail: The replacing email
    :return:
    """
    update_sql = "UPDATE email SET email = %s WHERE username = %s AND email = %s"
    exec_commit(update_sql, [newEmail, username, oldEmail])

def getEmail(username, email):
    """
    Gets a username/email pair
    :param username: The username in the pair
    :param email: The email in the pair
    :return: A tuple containing the username and email entries
    """
    return exec_get_one('SELECT * FROM email WHERE username = %s AND email = %s', [username, email])

def getEmailsByUser(username):
    """
    Gets all emails associated with a user
    :param username: The user whose emails we are getting
    :return: A tuple of emails associated with the user
    """
    return exec_get_all('SELECT email FROM email WHERE username = %s', [username])

def getUserByEmail(email):
    """
    Gets all users associated with the email
    :param email: The email whose user(s) we are finding
    :return: A tuple of users associated with the email
    """
    return exec_get_all('SELECT username FROM email WHERE email = %s', [email])