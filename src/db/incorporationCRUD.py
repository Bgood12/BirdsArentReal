from src.db.db_utils import *

def createIncorporation(recipe_id, ingredient_id, quantity):
    create_sql = "INSERT INTO incorporation (recipe_id, ingredient_id, quantity) VALUES (%s, %s, %s)"
    exec_commit(create_sql, [recipe_id, ingredient_id, quantity])

def getIncorporationsByRecipeID(recipe_id):
    get_sql = "SELECT * FROM incorporations WHERE recipe_id = %d"
    return exec_get_all(get_sql, [recipe_id])

def getIncorporationsByIngredientID(ingredient_id):
    get_sql = "SELECT * FROM incorporations WHERE ingredient_id = %d"
    return exec_get_all(get_sql, [ingredient_id])

def getIncorporation(recipe_id, ingredient_id):
    get_sql = "SELECT * FROM incorporations WHERE recipe_id = %d AND ingredient_id = %d"
    return exec_get_all(get_sql, [recipe_id, ingredient_id])    

def deleteIncorporation(recipe_id, ingredient_id):
    delete_sql = "DELETE FROM incorporation WHERE recipe_id = %d AND ingredient_id = %d"
    exec_commit(delete_sql, [recipe_id, ingredient_id])

def updateIncorporation(recipe_id, ingredient_id, quantity):
    update_sql = "UPDATE recipes SET quantity = %d WHERE recipe_id = %d AND ingredient_id = %d"
    exec_commit(update_sql, [recipe_id, ingredient_id, quantity])