from src.program_operations.accountOperations import *
from src.program_operations.recipeOperations import *


currentUser = None # global variable for storing the current user

def help(loggedin):
    # displays list of currently available commands
    if loggedin:
        print("Available commands:\nq - quits the application\nhelp - display available commands\nlogout - logs the current user out")
    else:
        helpmessage = "Available commands:\nq - quits the application\nhelp - display available commands\nlogin [username] [password] - logs the " \
                      "users into their accounts\nregister [username] [password] - registers a new user account\n"
        print(helpmessage)
def parseInput(input):
    command = input.split()
    global currentUser
    if command[0] == "help":
        help(currentUser is not None)
    # account operations
    if currentUser is None or not currentUser.isLoggedIn():
        if command[0] == "login" and len(command) == 3:
            currentUser = login(command[1], command[2])
        elif command[0] == "register" and len(command) == 3:
            createAccount(command[1], command[2])
    else:
        if command[0] == "logout":
            currentUser.logout()
        #elif:
            # beginning of recipe operations

