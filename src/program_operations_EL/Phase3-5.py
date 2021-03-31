from src.db.incorporationCRUD import *
from src.db.pantryCRUD import *


def recipeCanBeMade(recipe_id, username, scalar):
    incorperations = getIncorporationsByRecipeID(recipe_id)
    for incorp in incorperations:
        if not ampleIngredientStored(username, incorp[1], incorp[2] * scalar):
            return False
    return True


def ampleIngredientStored(username, ingredient_id, amount_needed):
    quantityInPantry = getAmountOfIngredient(username, ingredient_id)
    return amount_needed <= quantityInPantry