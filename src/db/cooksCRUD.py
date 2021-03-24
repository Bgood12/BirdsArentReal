from src.db.db_utils import *

import datetime

def cookRecipe(username, recipe_id, rating, servings):
    """
    User cooks a recipe. The date, servings, and rating is recorded.
    :param username: The user who cooked the recipe
    :param recipe_id: The recipe being cooked
    :param rating: The rating given by the user
    :param servings: The amount of servings cooked
    :return:
    """
    if not hasIngredients(username):
        print("The user does not have enough ingredients to cook this recipe")
        return

    creation_date = datetime.datetime.now() # The date the recipe was cooked
    create_sql = "INSERT INTO cooks (creation_date, username, recipe_id, rating, servings)"\
                 "VALUES (%s, %s, %d, %d, %d)"
    exec_commit(create_sql, [creation_date, username, recipe_id, rating, servings])

def listCookedRecipes(username):
    """
    Lists all recipes cooked by a user
    :param username: The name to search ccoked recipes history
    :return:
    """
    exec_get_all('SELECT username FROM cooks')

def recipeRequirements(recipe_id):
    """
    List the recipe ingredient requirements
    :param recipe_id: The recipe being checked
    :return:
    """
    return exec_get_one('SELECT ingredient_id FROM incorporates WHERE recipe_id = %s', [recipe_id])


def hasIngredients(username, recipe_id) -> bool:
    """
    Checks if the user has enough ingredients to cook recipe
    :param username: Name of the user checking ingredient requirements
    :return:
    """

    pantry = exec_get_one('SELECT ingredient_id FROM pantry WHERE username = %s', [username])
    ingredients = recipeRequirements(recipe_id)

    return bool(set(ingredients).intersection(pantry)) # Checks if the pantry has the needed ingredients




