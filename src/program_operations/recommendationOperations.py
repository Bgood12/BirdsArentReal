from src.db.incorporationCRUD import getIncorporationsByIngredientID
from src.db.pantryCRUD import getIngredientsByUser
from src.db.recipesCRUD import *
from src.program_operations.accountOperations import *
from src.program_operations_EL.Phase35 import recipeCanBeMade


def topFifty():
    return exec_get_all("SELECT * FROM recipes ORDER BY rating DESC LIMIT 50")

def topFiftyDates():
    return exec_get_all("SELECT recipes.recipe_id, recipes.recipe_name, authorship.creation_date FROM \
        recipes INNER JOIN authorship ON recipes.recipe_id=authorship.recipe_id ORDER BY authorship.creation_date DESC LIMIT 50")

def getAllMakable(username):
    userPantry = getIngredientsByUser(username)
    allRecipes = []
    for ingred in userPantry:
        recipes = getIncorporationsByIngredientID(ingred[0])
        for recip in recipes:
            if recip[0] not in allRecipes:
                allRecipes.append(recip[0])
                # should store all recipe ids that incorperate the given ingredient id
    allMakable = []
    for recipe_id in allRecipes:
        if recipeCanBeMade(recipe_id, username, 1):
            allMakable.append(getRecipeByID(recipe_id))
            # TODO discuss if we want to display recipes if the user has all needed ingredients but not for 1 full batch
    allMakable.sort(key=lambda x:x[2]) # sort by rating. This will likely be in ascending order
    allMakable.reverse() # reverse the list so it's from highest to lowest rating

    if len(allMakable) == 0:
        print("You do not have the needed ingredients for any stored recipes.")
        return
    for recipe in allMakable:
        strn = str(recipe[0]) + ", name: " + recipe[1] + ", rating: " + str(recipe[2])
        print(strn)