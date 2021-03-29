from src.db.db_utils import *
import datetime

def createAuthorship(username, recipe_id):
    creation_date = datetime.datetime.now()

    create_sql = "INSERT INTO authorship (username, recipe_id, creation_date) VALUES (%s, %d, %s)"
    exec_commit(create_sql, [username, recipe_id, creation_date])

def getAuthorshipByID(recipe_id):
    get_sql = "SELECT * FROM authorship WHERE recipe_id = %d"
    return exec_get_one(get_sql, [recipe_id])

def getAuthorshipsByName(username):
    get_sql = "SELECT * FROM authorship WHERE username = %s"
    return exec_get_all(get_sql, [username])

def deleteAuthorship(recipe_id):
    delete_sql = "DELETE FROM categories WHERE recipe_id = %d"
    exec_commit(delete_sql, [recipe_id])
