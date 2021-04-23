from src.db.db_utils import *

def createRecipe(name, description, cook_time, steps, difficulty):
    create_sql = "INSERT INTO recipes (recipe_name, description, cook_time, steps, difficulty)" \
                 "VALUES (%s, %s, %s, %s, %s)"
    exec_commit(create_sql, [name, description, cook_time, steps, difficulty])
    recipes = getRecipesByName(name)
    return recipes[-1]
    # return exec_commit(create_sql, [name, description, cook_time, steps, difficulty])
                 
def getRecipeByID(id):
    get_sql = "SELECT * FROM recipes WHERE recipe_id = %s"
    return exec_get_one(get_sql, [id])

def getRecipesByName(name):
    get_sql = "SELECT * FROM recipes WHERE recipe_name = %s"
    return exec_get_all(get_sql, [name])

def getRecipesByDifficulty(difficulty):
    get_sql = "SELECT * FROM recipes WHERE difficulty = %s"
    return exec_get_all(get_sql, [difficulty])

def deleteRecipe(id):
    delete_sql = "DELETE FROM recipes WHERE recipe_id = %s"
    exec_commit(delete_sql, [id])

def updateRecipeName(id, name):
    update_sql = "UPDATE recipes SET recipe_name = %s WHERE recipe_id = %s"
    exec_commit(update_sql, [name, id])

def updateRecipeRating(id, rating):
    update_sql = "UPDATE recipes SET rating = %s WHERE recipe_id = %s"
    exec_commit(update_sql, [rating, id])

def updateRecipeDescription(id, description):
    update_sql = "UPDATE recipes SET description = %s WHERE recipe_id = %s"
    exec_commit(update_sql, [description, id])

def updateRecipeCookTime(id, cook_time):
    update_sql = "UPDATE recipes SET cook_time = %s WHERE recipe_id = %s"
    exec_commit(update_sql, [cook_time, id])

def updateRecipeSteps(id, steps):
    update_sql = "UPDATE recipes SET steps = %s WHERE recipe_id = %s"
    exec_commit(update_sql, [steps, id])

def updateRecipeDifficulty(id, difficulty):
    update_sql = "UPDATE recipes SET difficulty = %s WHERE recipe_id = %s"
    exec_commit(update_sql, [difficulty, id])

def getRecipesLikeName(recipe_name):
    select_sql = "SELECT * FROM recipes WHERE recipe_name LIKE %s"
    recipe_name = "%" + recipe_name + "%"
    return exec_get_all(select_sql, [recipe_name])

def getRecommendedRecipes(username):
    select_sql = "SELECT DISTINCT * FROM recipes WHERE recipe_id = \
        (SELECT recipe_id FROM cooks WHERE NOT username = %s AND username = \
            (SELECT username FROM cooks WHERE recipe_id = \
                (SELECT recipe_id FROM cooks WHERE username = %s))) \
        ORDER BY rating"
    return exec_get_all(select_sql, [username])