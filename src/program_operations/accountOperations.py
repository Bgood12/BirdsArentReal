import secrets
from src.db.userCRUD import *


class CurrentUser():

    def __init__(self, username):
        self._username = username
        self._loggedIn = True

    def logout(self):
        self._loggedIn = False


def createAccount(username, password):
    createUser(username, password)


def login(username, password):
    hash = pwHash(password)
    user = exec_get_one("SELECT username FROM users WHERE username = %s AND password = %s", [username, hash])
    if user[0] == username:
        updateLastAccess(username, datetime.datetime.now())
        return CurrentUser.__init__(username=username)
    else:
        print("Invalid username or password")


def logout(curUser: CurrentUser):
    updateLastAccess(curUser._username, datetime.datetime.now())
    curUser.logout()


def pwHash(pw):
    return hashlib.sha256(pw.encode('utf-8')).hexdigest()  # The encoded password
