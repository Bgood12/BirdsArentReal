from src.db.recipesCRUD import *
from src.db.authorshipCRUD import *
from src.db.cooksCRUD import *
from src.db.categoriesCRUD import *
from src.program_operations.accountOperations import *


def newRecipe(currentUser: CurrentUser, name, description, cooktime, steps, difficulty):
    if currentUser.isLoggedIn():
        id = createRecipe(name, description, cooktime, steps, difficulty)[0] # Get the ID from the returned tuple
        createAuthorship(currentUser.getUser(), id)
        print("Recipe has been created")
    else:
        print("No user logged in to create the recipe")


def deleteMyRecipe(currentUser: CurrentUser, recipeID):
    if getAuthorshipByID(recipeID)[0] == currentUser.getUser() and currentUser.isLoggedIn():
        cooks = getChefsByRecipeCooked(recipeID)
        if len(cooks) != 0:
            print("This recipe cannot be deleted since a user has already cooked it")
            return
        deleteAuthorship(recipeID)
        deleteLinesInvolvingRecipeCategory(recipeID)
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
    updateRating(currentUser.getUser(), id, rating)
    newRating = 0
    allRatings = getRatingsByRecipeCooked(id)
    if len(allRatings) == 0:
        return
    for rat in allRatings:
        newRating += rat[0]
    newRating /= len(allRatings)
    updateRecipeRating(id, newRating)


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

def printMyHistory(currentUser: CurrentUser):
    myCooked = listCookedRecipes(currentUser.getUser())
    if(len(myCooked) == 0):
        print("Your cooking history is empty")
    print("id: name; your rating:average rating")
    for cookedRecipe in myCooked:
        recipe = getRecipeByID(cookedRecipe[0])
        myRating = getRatingByUserRecipe(currentUser.getUser(), recipe[0])
        print(str(recipe[0])+": "+recipe[1]+"; ("+str(myRating[0])+":"+str(recipe[2])+")")