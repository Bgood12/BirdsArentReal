from src.db.recipesCRUD import *
from src.db.authorshipCRUD import *
from src.program_operations.accountOperations import *


def newRecipe(currentUser: CurrentUser, name, description, cooktime, steps, difficulty):
    if currentUser.isLoggedIn():
        id = createRecipe(name, description, cooktime, steps, difficulty)[0] # Get the ID from the returned tuple
        createAuthorship(currentUser.getUser(), id)
        print("Recipe has been created")
    else:
        print("No user logged in to create the recipe")


def deleteMyRecipe(currentUser: CurrentUser, recipeID):
    if getAuthorshipByID(id)[0] == currentUser.getUser() and currentUser.isLoggedIn():
        deleteRecipe(recipeID)
        print("Recipe has been deleted")
    else:
        print("Current user did not create this recipe")


def changeRecipeName(currentUser: CurrentUser, id, name):
    if getAuthorshipByID(id)[0] == currentUser.getUser() and currentUser.isLoggedIn():
        updateRecipeName(id, name)
        print("The recipe's name has been updated")
    else:
        print("Current user did not create this recipe")


def changeRecipeRating(currentUser: CurrentUser, id, rating):
    if getAuthorshipByID(id)[0] == currentUser.getUser() and currentUser.isLoggedIn():
        updateRecipeRating(id, rating)
        print("The recipe's rating has been updated")
    else:
        print("Current user did not create this recipe")


def changeRecipeDescription(currentUser: CurrentUser, id, description):
    if getAuthorshipByID(id)[0] == currentUser.getUser() and currentUser.isLoggedIn():
        updateRecipeDescription(id, description)
        print("The recipe's description has been updated")
    else:
        print("Current user did not create this recipe")


def changeRecipeCookTime(currentUser: CurrentUser, id, cooktime):
    if getAuthorshipByID(id)[0] == currentUser.getUser() and currentUser.isLoggedIn():
        updateRecipeCookTime(id, cooktime)
        print("The recipe's cook time has been updated")
    else:
        print("Current user did not create this recipe")


def changeRecipeSteps(currentUser: CurrentUser, id, steps):
    if getAuthorshipByID(id)[0] == currentUser.getUser() and currentUser.isLoggedIn():
        updateRecipeSteps(id, steps)
        print("The recipe's steps have been updated")
    else:
        print("Current user did not create this recipe")


def changeRecipeDifficulty(currentUser: CurrentUser, id, difficulty):
    if getAuthorshipByID(id)[0] == currentUser.getUser() and currentUser.isLoggedIn():
        updateRecipeDifficulty(id, difficulty)
        print("The recipe's difficulty has been updated")
    else:
        print("Current user did not create this recipe")

def printMyRecipes(currentUser: CurrentUser):
    myRecipes = getAuthorshipsByName(currentUser.getUser())
    print("My Recipe List:")
    for recipe in myRecipes:
        recipeName = getRecipeByID(recipe[1])[1]
        authorshipToString = "" + str(recipe[1]) + ": " + recipeName
        print(authorshipToString)