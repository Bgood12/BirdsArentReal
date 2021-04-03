from src.program_operations.accountOperations import *
from src.program_operations.recipeOperations import *
from src.program_operations_EL.Phase35 import *
from src.program_operations.searchOperations import *
from src.program_operations.categoriesOperations import *
from src.program_operations_EL.memes import *
from src.db.incorporationCRUD import *

currentUser = None  # global variable for storing the current user


def helpcmd(loggedin):
    # displays list of currently available commands
    if loggedin:
        print("Available commands:\nquit - quits the application\nhelp - display available commands\nlogout - logs "
              "the current user out\ncreateRecipe - lets the user create a recipe\neditRecipe\ndeleteRecipe\ngetMyRecipes\n"
              "addRecipeIngredient\nremoveRecipeIngredient\neditRecipeIngredientQuantity\ncreateCategory\nlistCategories"
              "deleteCategory\naddRecipeInCategory\ndeleteRecipeInCategory\nsearch\ncookRecipe\ncanIMake\ngetMyPantry"
              "addIngredientToPantry\ndeletePantryEntry\nrr")
    else:
        helpmessage = "Available commands:\nquit - quits the application\nhelp - display available commands\nlogin - logs the " \
                      "users into their accounts\nregister - registers a new user account\n"
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
            logout(currentUser)

        # RECIPE OPERATIONS
        # CREATE A RECIPE
        elif command[0] == "createRecipe":
            recipeName = input("Enter the name of your new recipe: ")
            description = input("Enter a description: ")
            cook_time = float(input("Prep time in minutes: "))
            steps = input("What steps does it take to prepare? ")
            dif = 'very_medium'  # the most premium difficulty
            while not (dif == 'very_easy' or dif == 'easy' or dif == 'medium' or dif == 'hard' or dif == 'very_hard'):
                dif = input("Enter the new difficulty rating of this recipe: ")
            newRecipe(currentUser, recipeName, description, cook_time, steps, dif)
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
        elif command[0] == "deleteRecipe" or command[0] == "dr":
            recipeID = int(input("Enter the recipe you wish to delete: "))
            deleteMyRecipe(currentUser, recipeID)
        elif command[0] == "getMyRecipes" or command[0] == "gmr":
            printMyRecipes(currentUser)
        elif command[0] == "addRecipeIngredient" or command[0] == "ari":
            recipeID = int(input("Enter the recipe you want to change: "))
            ingredID = int(input("Enter the ingredient you want to add: "))
            quantity = float(input("Enter the quantity the recipe requires: "))
            createIncorporation(recipeID, ingredID, quantity)
            print("Ingredient "+ str(ingredID) + " has been added to Recipe " + str(recipeID))
        elif command[0] == "removeRecipeIngredient" or command[0] == "rri":
            recipeID = int(input("Enter the recipe you want to change: "))
            ingredID = int(input("Enter the ingredient you want to remove: "))
            deleteIncorporation(recipeID, ingredID)
            print("Ingredient " + str(ingredID) + " has been removed from Recipe " + str(recipeID))
        elif command[0] == "editRecipeIngredientQuantity" or command[0] == "eriq":
            recipeID = int(input("Enter the recipe you want to change: "))
            ingredID = int(input("Enter the ingredient you want to affect: "))
            quantity = float(input("Enter the updated quantity the recipe requires: "))
            updateIncorporation(recipeID, ingredID, quantity)
            print("Recipe "+str(recipeID)+" now requires "+str(quantity)+" stones of "+str(ingredID))
        # CATEGORY OPERATIONS
        # CREATE CATEGORY
        elif command[0] == "createCategory" or command[0] == "cc":
            categoryName = input("Enter the name of the category: ")
            recipeId = int(input("Enter a recipe ID to add: "))
            createNewCategory(currentUser, recipeId, categoryName)

        # LIST CATEGORIES
        elif command[0] == "listCategories":
            print("List of categories:\n")
            listAllCategories(currentUser.getUser())

        # DELETE CATEGORY
        elif command[0] == "deleteCategory":
            categoryName = input("Enter the name of the category to delete: ")
            deleteCategory(categoryName, currentUser.getUser())

        # ADD RECIPE IN CATEGORY
        elif command[0] == "addRecipeInCategory" or command[0] == "aric":
            categoryName = input("Enter name of category to add to: ")
            recipeId = int(input("Enter the id of the recipe to add: "))
            addToCategory(recipeId, categoryName, currentUser.getUser())
            print("Category " + categoryName + " assigned to " + str(recipeId))

        # DELETE RECIPE IN CATEGORY
        elif command[0] == "deleteRecipeInCategory" or command[0] == "dric":
            categoryName = input("Enter name of category to delete from: ")
            recipeId = int(input("Enter the id of the recipe to delete: "))
            deleteFromCategory(recipeId, categoryName, currentUser.getUser())
            print("Category " + categoryName + " removed from " + str(recipeId))

        # RECIPE SEARCH
        elif command[0] == "search" or command[0] == "s":
            key = input("Please choose a search format [categories, name, ingredients]: ")
            while not (key == "categories" or key == "name" or key == "ingredients"):
                key = input("Incorrect format please try again [categories, name, ingredients]: ")
            searchRecipe(key)

        # COOKING RELATED OPERATIONS
        # COOK A RECIPE
        elif command[0] == "cookRecipe" or command[0] == "cr":
            recipeID = int(input("Enter the ID of the recipe you wish to make: "))
            scalar = float(input("Enter the number by which you multiplied the recipe's ingredients: "))
            rating = int(input("Enter what you would rate this recipe on a scale of 0 to 5 "))
            if rating < 0:
                rating = 0
            elif rating > 5:
                rating = 5
            makeRecipe(recipeID, currentUser.getUser(), scalar, rating)
        # TELLS THE USER IF THEY CAN MAKE A RECIPE
        elif command[0] == "canIMake" or command[0] == "cim":
            recipeID = int(input("Enter the ID of the recipe you wish to make: "))
            scalar = float(input("How many times would you like to make this recipe: "))
            if recipeCanBeMade(recipeID, currentUser.getUser(), scalar):
                print("You have everything you need to make that volume of this recipe")
            else:
                print("You lack the required ingredients to make that volume of this recipe")

        # PANTRY OPERATIONS
        # PRINTS THE USER'S PANTRY
        elif command[0] == "getMyPantry" or command[0] == "gmp":
            printMyPantryStr(currentUser.getUser())
        # ADDS AN INGREDIENT TO THE USER'S PANTRY
        elif command[0] == "addIngredientToPantry" or command[0] == "aitp":
            purchaseDate = datetime.datetime.now()
            ingrID = int(input("Enter the Ingredient ID: "))
            quantity = float(input("Enter the quantity purchased: "))
            expirationDate = addDays(purchaseDate, int(input("Enter the number of days before it expires: ")))
            insertToPantry(purchaseDate, currentUser.getUser(), ingrID, quantity, expirationDate)
        # REMOVES AN INGREDIENT FROM THE USER'S PANTRY
        elif command[0] == "deletePantryEntry" or command[0] == "dpe":
            ingrID = int(input("Enter the ID of the ingredient you wish to delete: "))
            purchstr = "Enter the purchase date in this format: " + str(datetime.datetime.now())
            purchDate = datetime.datetime.fromisoformat(input(purchstr))
            deleteFromPantry(purchDate, currentUser.getUser(), ingrID)

        # MEME OPERATIONS
        elif command[0] == "rr" or command[0] == "rickroll":
            rickRoll()
        elif command[0] == "sb" or command[0] == "stickbug":
            stickbug()

