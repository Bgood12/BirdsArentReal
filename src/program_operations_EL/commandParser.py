from src.program_operations.accountOperations import *
from src.program_operations.recipeOperations import *

currentUser = None  # global variable for storing the current user


def help(loggedin):
    # displays list of currently available commands
    if loggedin:
        print(
            "Available commands:\nq - quits the application\nhelp - display available commands\nlogout - logs the current user out")
    else:
        helpmessage = "Available commands:\nq - quits the application\nhelp - display available commands\nlogin [username] [password] - logs the " \
                      "users into their accounts\nregister [username] [password] - registers a new user account\n"
        print(helpmessage)


def parseInput(inputStr):
    command = inputStr.split()
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
        elif command[0] == "createRecipe":
            # beginning of recipe operations
            recipeName = inputStr[12:]
            description = input("Enter a description: ")
            cook_time = float(input("Prep time in minutes: "))
            steps = input("What steps does it take to prepare? ")
            difficulty = input("How hard is it to prepare [very_easy to very_hard]? ")
            newRecipe(currentUser, recipeName, description, cook_time, steps, difficulty)
        elif command[0] == "editRecipe":
            recipeID = int(command[1])
            # TODO add prompt for which part of the recipe is being edited, then a prompt for the new value
        # TODO recipe operations: getMyRecipes (to view ids of recipes by the user), deleteRecipe [id]
        # TODO createCategoryForRecipe [recipeID] [new-category], assignToCategory [recipeID] [category]
        # TODO recipe search operations
        # TODO cooking the recipe related operations
        # TODO user pantry operations
