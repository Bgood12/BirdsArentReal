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
    creation_date = datetime.datetime.now() # The date the recipe was cooked
    create_sql = "INSERT INTO cooks (creation_date, username, recipe_id, rating, servings)"\
                 "VALUES (%s, %s, %s, %s, %s)"
    exec_commit(create_sql, [creation_date, username, recipe_id, rating, servings])
    
def updateRating(username, recipe_id, new_rating):
    """
    User updates their rating for a recipe.
    :param username: The user updating the rating
    :param recipe_id: The recipe being rated
    :param new_rating: The new rating
    :return:
    """
    update_sql = "UPDATE cooks SET rating = %s WHERE username = %s AND recipe_id = %s"
    user_cook = exec_get_one('SELECT * FROM cooks WHERE username = %s', [username])
    recipe = exec_get_one('SELECT * FROM user_cook WHERE recipe_id = %s', [recipe_id])
    exec_commit(update_sql, [new_rating, username, recipe_id])

def updateServings(username, recipe_id, new_servings):
    """
    User updates their servings for a recipe.
    :param username: The user updating the rating
    :param recipe_id: The recipe being rated
    :param new_rating: The new servings
    :return:
    """
    update_sql = "UPDATE recipe_id SET servings = %s WHERE servings = %s"
    user_cook = exec_get_one('SELECT * FROM cooks WHERE username = %s', [username])
    recipe = exec_get_one('SELECT * FROM user_cook WHERE recipe_id = %s', [recipe_id])
    exec_commit(update_sql, [new_servings, recipe])    

def listCookedRecipes(username):
    """
    Lists all recipes cooked by a user
    :param username: The name to search ccoked recipes history
    :return:
    """
    return exec_get_all('SELECT username FROM cooks', [username]) # <-- not how you do that, we'll fix it later


def getChefsByRecipeCooked(recipe_id):
    get_sql = "SELECT username FROM cooks WHERE recipe_id = %s"
    return exec_get_all(get_sql, [recipe_id])
