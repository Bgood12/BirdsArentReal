import secrets
from src.db.userCRUD import *


class CurrentUser():

    def __init__(self, username):
        self._username = username
        self._loggedIn = True

    def logout(self):
        self._loggedIn = False

    def isLoggedIn(self):
        return self._loggedIn

    def getUser(self):
        return self._username


def createAccount(username, password):
    createUser(username, password)


def login(username, password):
    """
    Logs into an account with a username and password
    :param username: The user of the account we are logging into
    :param password: the password of the account that we are logging into
    :return: A Current user object
    """
    hash = _pwHash(password)
    user = exec_get_one("SELECT username FROM users WHERE username = %s AND password = %s", [username, hash])
    if user[0] == username:
        updateLastAccess(username, datetime.datetime.now())
        return CurrentUser.__init__(username=username)
    else:
        print("Invalid username or password")


def logout(curUser: CurrentUser):
    updateLastAccess(curUser.getUser(), datetime.datetime.now())
    curUser.logout()


def _pwHash(pw):
    """
    Helper method to hash a password
    :param pw: The password being hashed
    :return: The hashed password
    """
    return hashlib.sha256(pw.encode('utf-8')).hexdigest()  # The encoded password
