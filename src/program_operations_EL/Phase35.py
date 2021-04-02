from src.db.incorporationCRUD import *
from src.db.pantryCRUD import *
from src.db.ingredientsCRUD import getIngredient
from src.db.cooksCRUD import *

# TODO ensure that errors do not occur when a value in the incorperation is not present in the pantry at all
def recipeCanBeMade(recipe_id, username, scalar):
    incorperations = getIncorporationsByRecipeID(recipe_id)
    for incorp in incorperations:
        if not ampleIngredientStored(username, incorp[1], incorp[2] * scalar):
            return False
    return True


def ampleIngredientStored(username, ingredient_id, amount_needed):
    quantityInPantry = getAmountOfIngredient(username, ingredient_id)
    return amount_needed <= quantityInPantry


def makeRecipe(recipe_id, username, scalar, rating):
    if recipeCanBeMade(recipe_id, username, scalar):
        cookRecipe(username, recipe_id, recipe_id, scalar)
        incorperations = getIncorporationsByRecipeID(recipe_id)
        for incorp in incorperations:
            useIngredientByClosestExpirationDate(username, incorp[1], incorp[2] * scalar)
        print("Congratulations on completing this recipe!")
    else:
        print("This recipe could not be completed due to inadequate ingredients")

def printMyPantryStr(username):
    print("Your pantry:")
    pantry = getPantryByUser(username)
    for ingr in pantry:
        ingredient = getIngredient(ingr[2])
        stringToPrint = "id:" + ingr[2] + ", quantity left: " + ingr[4] + " of " + ingr[5] + ", name: " + ingredient[1] + ", dates: " + ingr[0] + " to " + ingr[3]
        print(stringToPrint)