from src.program_operations.accountOperations import *
from src.program_operations.recipeOperations import *
from src.program_operations_EL.Phase35 import *
from src.program_operations.searchOperations import *
from src.program_operations.categoriesOperations import *
from src.program_operations_EL.memes import *

currentUser = None  # global variable for storing the current user


def helpcmd(loggedin):
    # displays list of currently available commands
    if loggedin:
        print("Available commands:\nquit - quits the application\nhelp - display available commands\nlogout - logs the current user out")
    else:
        helpmessage = "Available commands:\nquit - quits the application\nhelp - display available commands\nlogin [username] [password] - logs the " \
                      "users into their accounts\nregister [username] [password] - registers a new user account\n"
        print(helpmessage)


def parseInput(inputStr):
    command = inputStr.split()
    global currentUser
    if command[0] == "help":
        helpcmd(currentUser is not None)
    # ACCOUNT OPERATIONS
    if currentUser is None or not currentUser.isLoggedIn():
        if command[0] == "login":
            username = input("Username: ")
            password = input("Password: ")
            currentUser = login(username, password)
        elif command[0] == "register":
            username = input("Username: ")
            password = input("Password: ")
            createAccount(username, password)
    else:
        if command[0] == "logout":
            currentUser.logout()

        # RECIPE OPERATIONS
        # CREATE A RECIPE
        elif command[0] == "createRecipe":
            recipeName = input("Enter the name of your new recipe: ")
            description = input("Enter a description: ")
            cook_time = float(input("Prep time in minutes: "))
            steps = input("What steps does it take to prepare? ")
            difficulty = input("How hard is it to prepare [very_easy to very_hard]? ")
            newRecipe(currentUser, recipeName, description, cook_time, steps, difficulty)
        # EDITS A GIVEN RECIPE VIA SEVERAL PROMPTS
        elif command[0] == "editRecipe":
            recipeID = int(input("Enter the ID of the recipe you would like to edit: "))
            field = 'taco'
            while not (field == 'name' or field == 'description' or field == 'cook_time' or field == 'steps' or field == 'difficulty' or field == 'cancel'):
                field = input("Enter the field you wish to edit [name,description,cook_time,steps,difficulty]: ")
            if field == 'name':
                newName = input("Enter the new name of this recipe: ")
                changeRecipeName(currentUser, recipeID, newName)
            elif field == 'description':
                newDescription = input("Enter the new description of this recipe: ")
                changeRecipeDescription(currentUser, recipeID, newDescription)
            elif field == 'cook_time':
                newCookTime = int(input("Enter the revised cook time: "))
                changeRecipeCookTime(currentUser, recipeID, newCookTime)
            elif field == 'steps':
                newSteps = input("Enter a revised series of steps: ")
                changeRecipeSteps(currentUser, recipeID, newSteps)
            elif field == 'difficulty':
                dif = 'very_medium' # the most premium difficulty
                while not (dif == 'very_easy' or dif == 'easy' or dif == 'medium' or dif == 'hard' or dif == 'very_hard'):
                    dif = input("Enter the new difficulty rating of this recipe: ")
                changeRecipeDifficulty(currentUser, recipeID, dif)
        elif command[0] == "deleteRecipe":
            recipeID = int(input("Enter the recipe you wish to delete: "))
            deleteMyRecipe(currentUser, recipeID)
        elif command[0] == "getMyRecipes":
            printMyRecipes(currentUser)

        # CATEGORY OPERATIONS
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

        # COOKING RELATED OPERATIONS
        # COOK A RECIPE
        elif command[0] == "cookRecipe":
            recipeID = int(input("Enter the ID of the recipe you wish to make: "))
            scalar = float(input("Enter the number by which you multiplied the recipe's ingredients: "))
            rating = int(input("Enter what you would rate this recipe on a scale of 0 to 5 "))
            if rating < 0:
                rating = 0
            elif rating > 5:
                rating = 5
            makeRecipe(recipeID, currentUser.getUser(), scalar, rating)
        # TELLS THE USER IF THEY CAN MAKE A RECIPE
        elif command[0] == "canIMake":
            recipeID = int(input("Enter the ID of the recipe you wish to make: "))
            scalar = float(input("How many times would you like to make this recipe: "))
            if recipeCanBeMade(recipeID, scalar):
                print("You have everything you need to make that volume of this recipe")
            else:
                print("You lack the required ingredients to make that volume of this recipe")

        # PANTRY OPERATIONS
        # PRINTS THE USER'S PANTRY
        elif command[0] == "getMyPantry":
            printMyPantryStr(currentUser.getUser())
        # ADDS AN INGREDIENT TO THE USER'S PANTRY
        elif command[0] == "addIngredientToPantry":
            purchaseDate = datetime.datetime.now()
            ingrID = int(input("Enter the Ingredient ID: "))
            quantity = float(input("Enter the quantity purchased"))
            expirationDate = addDays(purchaseDate, int(input("Enter the number of days before it expires")))
            insertToPantry(purchaseDate, currentUser.getUser(), ingrID, quantity, expirationDate)
        # REMOVES AN INGREDIENT FROM THE USER'S PANTRY
        elif command[0] == "deletePantryEntry":
            ingrID = int(input("Enter the ID of the ingredient you wish to delete: "))
            purchstr = "Enter the purchase date in this format: yyyy-mm-dd hh:mm-ss"
            purchDate = datetime.datetime.fromisoformat(input(purchstr))
            deleteFromPantry(purchDate, currentUser.getUser(), ingrID)

        # MEME OPERATIONS
        elif command[0] == "rr" or command[0] == "rickroll":
            rickRoll()

