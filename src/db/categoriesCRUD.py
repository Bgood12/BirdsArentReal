from src.db.db_utils import *

def createCategory(username, category_name):
    """
    Creates a new category of recipes
    :param category_name: The name of the category being created
    :return:
    """

    if not uniqueCategory(category_name): # Checks if the category is unique
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

def addRecipe(recipe_id, category_name, username):
    """
    Adds a recipe to the chosen category
    :param category_name: The category receiving a new recipe
    :param recipe_id: The recipe being added
    :param username: The name of the author user
    :return:
    """
    insert_sql = "INSERT INTO categories (recipe_id, category_name) VALUES (%d, %s)"
    exec_commit(insert_sql, [recipe_id, category_name])

def deleteRecipe(recipe_id, category_name):
    """
    Removes a recipe from a category
    :param recipe_id: The recipe to be removed
    :param category_name: The category being used
    :return:
    """
    exec_commit('DELETE FROM categories WHERE recipe_id = %d AND category_name = %s', [recipe_id, category_name])

def listCategoriesByUser(username):
    """
    Gets all the categories from the category table
    :return: A tuple containing all category names
    """
    return exec_get_all('SELECT category_name FROM categories WHERE username = %s', [username])

def listRecipes(category_name):
    return exec_get_all('SELECT recipe_id FROM categories where category_name = %s', [category_name])

def uniqueCategory(category_name) -> bool:
    """
    Checks if the category name is unique
    :param category_name: The name of the category being checked
    :return:
    """

    categories = listCategories() # List of all categories
    for category in categories[0]: # For each tuple in categories
        if category[0] == category_name:
            return False # The name of the category is not unique
    return True # The name of the category is unique

