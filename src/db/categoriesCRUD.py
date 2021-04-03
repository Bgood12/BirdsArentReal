from src.db.db_utils import *

def createCategory(username, category_name):
    """
    Creates a new category of recipes
    :param category_name: The name of the category being created
    :return:
    """

    if not uniqueCategory(category_name, username): # Checks if the category is unique
        print("This category has already been created.")
        return

    create_sql = "INSERT INTO categories (username, category_name) VALUES (%s, %s)"
    exec_commit(create_sql, [username, category_name])

def getUserCategory(username, category_name):
    """
    Gets a category by its name and corresponding username
    :param category_name: The category name to grab
    :param username: The name of the author user
    :return:
    """
    return exec_get_one('SELECT * FROM categories WHERE username = %s AND category_name = %s', [username, category_name])

def deleteUserCategory(username, category_name):
    """
    Deletes a category by its name and corresponding username
    :param category_name: The category name to remove
    :param username: The name of the author user
    :return:
    """
    exec_commit('DELETE FROM categories WHERE username = %s category_name = %s', [username, category_name])

def listCategoriesByUser(username):
    """
    Gets all the categories from the category table
    :return: A tuple containing all category names
    """
    return exec_get_all('SELECT category_name FROM categories WHERE username = %s', [username])

def uniqueCategory(category_name, username) -> bool:
    """
    Checks if the category name is unique
    :param category_name: The name of the category being checked
    :return:
    """

    categories = listCategoriesByUser(username) # List of all categories
    for category in categories: # For each tuple in categories
        if category[0] == category_name:
            return False # The name of the category is not unique
    return True # The name of the category is unique

def deleteLinesInvolvingRecipeCategory(recipe_id): # NAME BAD< WILL NOT FIX
    del_sql = "DELETE FROM categories WHERE recipe_id = %s"
    exec_commit(del_sql, [recipe_id])
