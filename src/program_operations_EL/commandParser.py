from src.program_operations.accountOperations import *
from src.program_operations.recipeOperations import *
from src.program_operations_EL.Phase35 import *
from src.program_operations.searchOperations import *
from src.program_operations.categoriesOperations import *
from src.program_operations_EL.memes import *
from src.db.incorporationCRUD import *
from src.program_operations.recommendationOperations import *
from src.program_operations_EL.safeInput import *

currentUser = None  # global variable for storing the current user


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
        elif command[0] == "createRecipe" or command[0] == "crr":
            createRecipeCmd(currentUser)
        # EDITS A GIVEN RECIPE VIA SEVERAL PROMPTS
        elif command[0] == "editRecipe":
            editRecipeCmd(currentUser)
        elif command[0] == "deleteRecipe" or command[0] == "dr":
            recipeID = getIntPositive("Enter the recipe you wish to delete: ")
            deleteMyRecipe(currentUser, recipeID)
        elif command[0] == "getMyRecipes" or command[0] == "gmr":
            printMyRecipes(currentUser)
        elif command[0] == "addRecipeIngredient" or command[0] == "ari":
            addRecipeIngredientCmd()
        elif command[0] == "removeRecipeIngredient" or command[0] == "rri":
            removeRecipeIngredientCmd()
        elif command[0] == "editRecipeIngredientQuantity" or command[0] == "eriq":
            editRecipeIngredientQuantityCmd()
        # CATEGORY OPERATIONS
        # CREATE CATEGORY
        elif command[0] == "createCategory" or command[0] == "cc":
            categoryName = input("Enter the name of the category: ")
            createNewCategory(currentUser, categoryName)

        # LIST CATEGORIES
        elif command[0] == "listCategories":
            print("List of categories:\n")
            listAllCategories(currentUser.getUser())

        # DELETE CATEGORY
        elif command[0] == "deleteCategory":
            categoryName = input("Enter the name of the category to delete: ")
            deleteCategory(currentUser.getUser(), categoryName)
            print("Category deleted")

        # ADD RECIPE IN CATEGORY
        elif command[0] == "addRecipeInCategory" or command[0] == "aric":
            categoryName = input("Enter name of category to add to: ")
            recipeId = getIntPositive("Enter the id of the recipe to add: ")
            addToCategory(recipeId, categoryName, currentUser.getUser())
            print("Category " + categoryName + " assigned to " + str(recipeId))

        # DELETE RECIPE IN CATEGORY
        elif command[0] == "deleteRecipeInCategory" or command[0] == "dric":
            categoryName = input("Enter name of category to delete from: ")
            recipeId = getIntPositive("Enter the id of the recipe to delete: ")
            deleteFromCategory(recipeId, categoryName, currentUser.getUser())
            print("Category " + categoryName + " removed from " + str(recipeId))

        # RECIPE SEARCH
        elif command[0] == "search" or command[0] == "s":
            key = input("Please choose a search format [categories, name, ingredients]: ")
            while not (key == "categories" or key == "name" or key == "ingredients"):
                key = input("Incorrect format please try again [categories, name, ingredients]: ")
            surt = input("Please choose a sort format [date, rating, alphabetical]: ")
            if not (surt == "date" or surt == "rating"):
                surt = "alf"
            searchRecipe(key, surt)

        # COOKING RELATED OPERATIONS
        # COOK A RECIPE
        elif command[0] == "cookRecipe" or command[0] == "cr":
            cookRecipeCmd(currentUser)
        # TELLS THE USER IF THEY CAN MAKE A RECIPE
        elif command[0] == "canIMake" or command[0] == "cim":
            canIMakeCmd(currentUser)
        elif command[0] == "updateRating" or command[0] == "ur":
            recipe_id = getIntPositive("Please input the id of the recipe whose rating you'd like to change: ")
            rating = getFloatPositive(0, 5, "input your new rating: ")
            changeRecipeRating(currentUser, recipe_id, rating)
        elif command[0] == "getMyHistory" or command[0] == "gmh":
            printMyHistory(currentUser)

        # PANTRY OPERATIONS
        # PRINTS THE USER'S PANTRY
        elif command[0] == "getMyPantry" or command[0] == "gmp":
            printMyPantryStr(currentUser.getUser())
        # ADDS AN INGREDIENT TO THE USER'S PANTRY
        elif command[0] == "addIngredientToPantry" or command[0] == "aitp":
            addIngredientToPantryCmd(currentUser)
        # REMOVES AN INGREDIENT FROM THE USER'S PANTRY
        elif command[0] == "deletePantryEntry" or command[0] == "dpe":
            deletePantryEntryCmd(currentUser)

        # MISC MISSING OPERATIONS
        # VIEW A SINGLE RECIPE
        elif command[0] == "viewRecipe" or command[0] == "vr":
            recipeID = getIntPositive("Enter the ID of the recipe you wish to view: ")
            printOneRecipe(recipeID)
        elif command[0] == "addIngredient" or command[0] == "ai":
            addIngredientCmd()
        elif command[0] == "deleteIngredient" or command[0] == "di":
            deleteIngredientCmd()
        # PHASE 4 OPERATIONS
        # DISPLAYS RECIPES THE USER CAN MAKE 1 BATCH OF
        elif command[0] == "deleteIngredientFromPantry" or command[0] == "difp":
            deletePantryEntryCmd(currentUser)

        # MISC MISSING OPERATIONS
        # VIEW A SINGLE RECIPE
        elif command[0] == "viewRecipe" or command[0] == "vr":
            recipeID = getIntPositive("Enter the ID of the recipe you wish to view: ")
            printOneRecipe(recipeID)
        # PHASE 4 OPERATIONS
        # DISPLAYS RECIPES THE USER CAN MAKE 1 BATCH OF
        elif command[0] == "getRecipiesOnHand" or command[0] == "groh":
            getAllMakable(currentUser.getUser())

        # RATING OPERATIONS
        # RETURNS THE 50 HIGHEST RATED RECIPES
        elif command[0] == "topFifty" or command[0] == "top50":
            print(topFifty())

        # MEME OPERATIONS
        elif command[0] == "rr" or command[0] == "rickroll":
            rickRoll()
        elif command[0] == "sb" or command[0] == "stickbug":
            stickbug()


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


# TODO move everything into helper methods like this
def printOneRecipe(recipe_id):
    rec = getRecipeByID(recipe_id)
    titleStr = str(rec[0]) + ": " + str(rec[1])
    ingreds = getIncorporationsByRecipeID(recipe_id)
    ingredStr = "ingredients (id:###): "
    for incorp in ingreds:
        ingredStr += "("+str(incorp[1])+":"+str(incorp[2])+") "
    print(titleStr)
    print("rating: "+str(rec[2]))
    print(ingredStr)
    print("description: "+rec[3])
    print("cook time: "+str(rec[4]))
    print("steps: "+rec[5])
    print("difficulty: "+rec[6])


def createRecipeCmd(currentUser1):
    recipeName = input("Enter the name of your new recipe: ")
    description = input("Enter a description: ")
    cook_time = getFloatPositive(0, 0, "Prep time in minutes: ")
    steps = input("What steps does it take to prepare? ")
    dif = getValidDifficulty("Enter the new difficulty rating of this recipe: ")
    newRecipe(currentUser1, recipeName, description, cook_time, steps, dif)

def editRecipeCmd(currentUser1):
    recipeID = getIntPositive("Enter the ID of the recipe you would like to edit: ")
    field = 'taco'
    while not (
            field == 'name' or field == 'description' or field == 'cook_time' or field == 'steps' or field == 'difficulty' or field == 'cancel'):
        field = input("Enter the field you wish to edit [name,description,cook_time,steps,difficulty]: ")
    if field == 'name':
        newName = input("Enter the new name of this recipe: ")
        changeRecipeName(currentUser1, recipeID, newName)
    elif field == 'description':
        newDescription = input("Enter the new description of this recipe: ")
        changeRecipeDescription(currentUser1, recipeID, newDescription)
    elif field == 'cook_time':
        newCookTime = getIntPositive("Enter the revised cook time: ")
        changeRecipeCookTime(currentUser1, recipeID, newCookTime)
    elif field == 'steps':
        newSteps = input("Enter a revised series of steps: ")
        changeRecipeSteps(currentUser1, recipeID, newSteps)
    elif field == 'difficulty':
        dif = getValidDifficulty("Enter the new difficulty rating of this recipe: ")
        changeRecipeDifficulty(currentUser1, recipeID, dif)
# TODO might not check for recipe ownership
def addRecipeIngredientCmd():
    recipeID = getIntPositive("Enter the recipe you want to change: ")
    ingredID = getIntPositive("Enter the ingredient you want to add: ")
    quantity = getFloatPositive(0, 0, "Enter the quantity the recipe requires: ")
    createIncorporation(recipeID, ingredID, quantity)
    print("Ingredient " + str(ingredID) + " has been added to Recipe " + str(recipeID))
# TODO might not check for recipe ownership
def removeRecipeIngredientCmd():
    recipeID = getIntPositive("Enter the recipe you want to change: ")
    ingredID = getIntPositive("Enter the ingredient you want to remove: ")
    deleteIncorporation(recipeID, ingredID)
    print("Ingredient " + str(ingredID) + " has been removed from Recipe " + str(recipeID))
# TODO might not check for recipe ownership
def editRecipeIngredientQuantityCmd():
    recipeID = getIntPositive("Enter the recipe you want to change: ")
    ingredID = getIntPositive("Enter the ingredient you want to affect: ")
    quantity = getFloatPositive(0, 0, "Enter the updated quantity the recipe requires: ")
    updateIncorporation(recipeID, ingredID, quantity)
    print("Recipe " + str(recipeID) + " now requires " + str(quantity) + " stones of " + str(ingredID))

def cookRecipeCmd(currentUser1):
    recipeID = getIntPositive("Enter the ID of the recipe you wish to make: ")
    scalar = getFloatPositive(.01, .01, "Enter the number by which you multiplied the recipe's ingredients: ")
    rating = getIntPositive("Enter what you would rate this recipe on a scale of 0 to 5 ")
    if rating < 0:
        rating = 0
    elif rating > 5:
        rating = 5
    makeRecipe(recipeID, currentUser1.getUser(), scalar, rating)
    changeRecipeRating(currentUser1, recipeID, rating)

def canIMakeCmd(currentUser1):
    recipeID = getIntPositive("Enter the ID of the recipe you wish to make: ")
    scalar = getFloatPositive(.01, .01, "How many times would you like to make this recipe: ")
    if recipeCanBeMade(recipeID, currentUser1.getUser(), scalar):
        print("You have everything you need to make that volume of this recipe")
    else:
        print("You lack the required ingredients to make that volume of this recipe")

def addIngredientToPantryCmd(currentUser1):
    purchaseDate = datetime.datetime.now()
    ingrID = getIntPositive("Enter the Ingredient ID: ")
    quantity = getFloatPositive(.01,.01, "Enter the quantity purchased: ")
    expirationDate = addDays(purchaseDate, int(input("Enter the number of days before it expires: ")))
    insertToPantry(purchaseDate, currentUser1.getUser(), ingrID, quantity, expirationDate)

def deletePantryEntryCmd(currentUser1):
    ingrID = getIntPositive("Enter the ID of the ingredient you wish to delete: ")
    purchstr = "Enter the purchase date in this format: " + str(datetime.datetime.now())
    purchDate = datetime.datetime.fromisoformat(input(purchstr))
    deleteFromPantry(purchDate, currentUser1.getUser(), ingrID)

# def addIngredientCmd():

# TODO move everything into helper methods like this
def printOneRecipe(recipe_id):
    rec = getRecipeByID(recipe_id)
    titleStr = str(rec[0]) + ": " + str(rec[1])
    ingreds = getIncorporationsByRecipeID(recipe_id)
    ingredStr = "ingredients (id:###): "
    for incorp in ingreds:
        ingredStr += "("+str(incorp[1])+":"+str(incorp[2])+") "
    print(titleStr)
    print("rating: "+str(rec[2]))
    print(ingredStr)
    print("description: "+rec[3])
    print("cook time: "+str(rec[4]))
    print("steps: "+rec[5])
    print("difficulty: "+rec[6])


def createRecipeCmd(currentUser1):
    recipeName = input("Enter the name of your new recipe: ")
    description = input("Enter a description: ")
    cook_time = getFloatPositive(0, 0, "Prep time in minutes: ")
    steps = input("What steps does it take to prepare? ")
    dif = getValidDifficulty("Enter the new difficulty rating of this recipe: ")
    newRecipe(currentUser1, recipeName, description, cook_time, steps, dif)

def editRecipeCmd(currentUser1):
    recipeID = getIntPositive("Enter the ID of the recipe you would like to edit: ")
    field = 'taco'
    while not (
            field == 'name' or field == 'description' or field == 'cook_time' or field == 'steps' or field == 'difficulty' or field == 'cancel'):
        field = input("Enter the field you wish to edit [name,description,cook_time,steps,difficulty]: ")
    if field == 'name':
        newName = input("Enter the new name of this recipe: ")
        changeRecipeName(currentUser1, recipeID, newName)
    elif field == 'description':
        newDescription = input("Enter the new description of this recipe: ")
        changeRecipeDescription(currentUser1, recipeID, newDescription)
    elif field == 'cook_time':
        newCookTime = getIntPositive("Enter the revised cook time: ")
        changeRecipeCookTime(currentUser1, recipeID, newCookTime)
    elif field == 'steps':
        newSteps = input("Enter a revised series of steps: ")
        changeRecipeSteps(currentUser1, recipeID, newSteps)
    elif field == 'difficulty':
        dif = getValidDifficulty("Enter the new difficulty rating of this recipe: ")
        changeRecipeDifficulty(currentUser1, recipeID, dif)
# TODO might not check for recipe ownership
def addRecipeIngredientCmd():
    recipeID = getIntPositive("Enter the recipe you want to change: ")
    ingredID = getIntPositive("Enter the ingredient you want to add: ")
    quantity = getFloatPositive(0, 0, "Enter the quantity the recipe requires: ")
    createIncorporation(recipeID, ingredID, quantity)
    print("Ingredient " + str(ingredID) + " has been added to Recipe " + str(recipeID))
# TODO might not check for recipe ownership
def removeRecipeIngredientCmd():
    recipeID = getIntPositive("Enter the recipe you want to change: ")
    ingredID = getIntPositive("Enter the ingredient you want to remove: ")
    deleteIncorporation(recipeID, ingredID)
    print("Ingredient " + str(ingredID) + " has been removed from Recipe " + str(recipeID))
# TODO might not check for recipe ownership
def editRecipeIngredientQuantityCmd():
    recipeID = getIntPositive("Enter the recipe you want to change: ")
    ingredID = getIntPositive("Enter the ingredient you want to affect: ")
    quantity = getFloatPositive(0, 0, "Enter the updated quantity the recipe requires: ")
    updateIncorporation(recipeID, ingredID, quantity)
    print("Recipe " + str(recipeID) + " now requires " + str(quantity) + " stones of " + str(ingredID))

def canIMakeCmd(currentUser1):
    recipeID = getIntPositive("Enter the ID of the recipe you wish to make: ")
    scalar = getFloatPositive(.01, .01, "How many times would you like to make this recipe: ")
    if recipeCanBeMade(recipeID, currentUser1.getUser(), scalar):
        print("You have everything you need to make that volume of this recipe")
    else:
        print("You lack the required ingredients to make that volume of this recipe")

def addIngredientToPantryCmd(currentUser1):
    purchaseDate = datetime.datetime.now()
    ingrID = getIntPositive("Enter the Ingredient ID: ")
    quantity = getFloatPositive(.01,.01, "Enter the quantity purchased: ")
    expirationDate = addDays(purchaseDate, int(input("Enter the number of days before it expires: ")))
    insertToPantry(purchaseDate, currentUser1.getUser(), ingrID, quantity, expirationDate)

def deletePantryEntryCmd(currentUser1):
    ingrID = getIntPositive("Enter the ID of the ingredient you wish to delete: ")
    purchstr = "Enter the purchase date in this format: " + str(datetime.datetime.now())
    purchDate = datetime.datetime.fromisoformat(input(purchstr))
    deleteFromPantry(purchDate, currentUser1.getUser(), ingrID)

def addIngredientCmd():
    ingred_name = input("Enter new ingredient name: ")
    ingred_aisle = input("Enter the aisle of the new ingredient: ")
    insertIngredient(ingred_name, ingred_aisle)
    print("Ingredient " + ingred_name + " has been added to " + ingred_aisle)

def deleteIngredientCmd():
    ingrID = getIntPositive("Enter the ID of the ingredient you wish to delete: ")
    if len(getIncorporationsByIngredientID(ingrID)) > 0:
        print("Ingredient could not be deleted since it is used in at least one recipe")
        return
    if getIngredientInAnyPantryCount(ingrID) > 0:
        print("Ingredient could not be deleted since it exists in a user's pantry")
        return
    deleteIngredient(ingrID)
    print("If the ingredient existed, it has been deleted")