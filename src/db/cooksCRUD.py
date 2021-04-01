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
                 "VALUES (%s, %s, %d, %d, %d)"
    exec_commit(create_sql, [creation_date, username, recipe_id, rating, servings])
    
def updateRating(username, recipe_id, new_rating):
    """
    User updates their rating for a recipe.
    :param username: The user updating the rating
    :param recipe_id: The recipe being rated
    :param new_rating: The new rating
    :return:
    """
    update_sql = "UPDATE cooks SET rating = %d WHERE rating = %d"
    exec_commit(update_sql, [new_rating, cooks])

def updateServings(username, recipe_id, new_servings):
    """
    User updates their servings for a recipe.
    :param username: The user updating the rating
    :param recipe_id: The recipe being rated
    :param new_rating: The new servings
    :return:
    """
    update_sql = "UPDATE cooks SET servings = %d WHERE servings = %d"
    exec_commit(update_sql, [new_servings, cooks])    

def listCookedRecipes(username):
    """
    Lists all recipes cooked by a user
    :param username: The name to search ccoked recipes history
    :return:
    """
    return exec_get_all('SELECT username FROM cooks')





