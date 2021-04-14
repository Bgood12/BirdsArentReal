from src.db.recipesCRUD import *
from src.db.authorshipCRUD import *
from src.program_operations.accountOperations import *

def topFifty():
    return exec_get_all("SELECT * FROM recipes ORDER BY rating DESC LIMIT 50")

def topFiftyDates():
    recipes_sorted = []
    recipes = exec_get_all("SELECT recipe_id FROM authorship ORDER BY creation_date DESC LIMIT 50")
    recipes = recipes[0]  # the ids of the recipes
    for recipe_id in recipes:
        recipe = getRecipeByID(recipe_id)
        recipes_sorted.append(recipe)
    return recipes_sorted
