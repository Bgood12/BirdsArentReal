from src.db.db_utils import *

def addRecipeToCategory(recipe_id, category_name, username):
    create_sql = "INSERT INTO belongs (recipe_id, category_name, username) VALUES (%s, %s, %s)"
    exec_commit(create_sql, [recipe_id, category_name, username])

def deleteRecipeFromCategory(recipe_id, category_name, username):
    delete_sql = "DELETE FROM belongs WHERE recipe_id = %s AND category_name = %s AND username = %s"
    exec_commit(delete_sql, [recipe_id, category_name, username])

def listRecipesByCategory(category_name, username):
    get_sql = "SELECT * FROM belongs WHERE category_name = %s and username = %s"
    exec_get_all(get_sql, [category_name, username])
