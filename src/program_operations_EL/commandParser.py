from src.program_operations.accountOperations import *
from src.program_operations.recipeOperations import *
from src.program_operations_EL.Phase35 import *
from src.program_operations.searchOperations import *
from src.program_operations.categoriesOperations import *

currentUser = None  # global variable for storing the current user


def helpcmd(loggedin):
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
        helpcmd(currentUser is not None)
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
        # CREATE CATEGORY
        elif command[0] == "createCategory":
            categoryName = input("Enter the name of the category: ")
            recipeId = int(input("Enter a recipe ID to add: "))
            createNewCategory(currentUser, recipeId, categoryName)

        # EDIT CATEGORY NAME
        elif command[0] == "editCategory":
            categoryName = input("Enter name of category you want to change: ")
            categoryNewName = input("Enter new name of the category: ")
            changeCategoryName(categoryName, categoryNewName)

        # LIST CATEGORIES
        elif command[0] == "listCategories":
            print("List of categories:\n")
            listAllCategories()

        # DELETE CATEGORY
        elif command[0] == "deleteCategory":
            categoryName = input("Enter the name of the category to delete: ")
            deleteCategory(categoryName)

        # ADD RECIPE IN CATEGORY
        elif command[0] == "addRecipeInCategory":
            categoryName = input("Enter name of category to add to: ")
            recipeId = int(input("Enter the id of the recipe to add: "))
            addNewRecipe(recipeId, categoryName)

       # DELETE RECIPE IN CATEGORY
        elif command[0] == "deleteRecipeInCategory":
            categoryName = input("Enter name of category to delete from: ")
            recipeId = int(input("Enter the id of the recipe to delete: "))
            deleteOldRecipe(recipeId, categoryName)

        # RECIPE SEARCH
        elif command[0] == "search":
            key = input("Please choose a search format [categories, name, ingredients]: ")
            while key != "categories" or key != "name" or key != "ingredients":
                key = input("Incorrect format please try again [categories, name, ingredients]: ")
            searchRecipe(key)

        # TODO cooking the recipe related operations
        elif command[0] == "cookRecipe":
            recipeID = int(input("Enter the ID of the recipe you wish to make: "))
            scalar = float(input("Enter the number by which you multiplied the recipe's ingredients: "))
            rating = int(input("Enter what you would rate this recipe on a scale of 0 to 5 "))
            if rating < 0:
                rating = 0
            elif rating > 5:
                rating = 5
            makeRecipe(recipeID, currentUser.getUser(), scalar, rating)
        elif command[0] == "canIMake":
            recipeID = int(input("Enter the ID of the recipe you wish to make: "))
            scalar = float(input("How many times would you like to make this recipe: "))
            if(recipeCanBeMade(recipeID, scalar)):
                print("You have everything you need to make that volume of this recipe")
            else:
                print("You lack the required ingredients to make that volume of this recipe")
        # TODO user pantry operations
        elif command[0] == "getMyPantry":
            printMyPantryStr(currentUser.getUser())
        elif command[0] == "addIngredientToPantry":
            purchaseDate = datetime.datetime.now()
            ingrID = int(input("Enter the Ingredient ID: "))
            quantity = float(input("Enter the quantity purchased"))
            expirationDate = addDays(purchaseDate, int(input("Enter the number of days before it expires")))
            insertToPantry(purchaseDate, currentUser.getUser(), ingrID, quantity, expirationDate)
        elif command[0] == "deletePantryEntry":
            ingrID = int(input("Enter the ID of the ingredient you wish to delete: "))
            purchstr = "Enter the purchase date in this format: yyyy-mm-dd hh:mm-ss"
            purchDate = datetime.datetime.fromisoformat(input(purchstr))
            deleteFromPantry(purchDate, currentUser.getUser(), ingrID)

