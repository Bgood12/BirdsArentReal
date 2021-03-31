from src.db.incorporationCRUD import *
from src.db.pantryCRUD import *

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


def makeRecipe(recipe_id, username, scalar):
    if recipeCanBeMade(recipe_id, username, scalar):
        incorperations = getIncorporationsByRecipeID(recipe_id)
        for incorp in incorperations:
            useIngredientByClosestExpirationDate(username, incorp[1], incorp[2] * scalar)
    else:
        print("This recipe could not be completed due to inadequate ingredients")