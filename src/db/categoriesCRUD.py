from src.db.db_utils import *

def createCategory(recipe_id, name):
    """
    Creates a new category of recipes
    :param name: The name of the category being created
    :return:
    """

    if not uniqueCategory(name):
        print("This category has already been created.")
        return

    create_sql = "INSERT INTO categories (recipe_id, name) VALUES (%d, %s)"
    exec_commit(create_sql, [recipe_id, name])

def getCategoryByName(name):
    """
    Gets a category by its name
    :param name: The category name to grab
    :return:
    """
    return exec_get_one('SELECT * FROM categories WHERE name = %s', [name])

def deleteCategoryByName(name):
    """
    Deletes a category by its name
    :param name: The category to be deleted
    :return:
    """
    exec_commit('DELETE FROM categories WHERE name = %s', [name])

def updateCategory(name, new_name = ''):
    """
    Updates the name of a category
    :param name: The current name of the category
    :param newName: The categories new name to be given
    :return:
    """
    if new_name:
        if not uniqueCategory(new_name):
            print("This category has already been created.")
            return
    else:
        new_name = name

    update_sql = "UPDATE categories SET name = %s"
    exec_commit(update_sql, [new_name, name])

def addRecipe(recipe_id, name):
    """
    Adds a recipe to the chosen category
    :param name: The category receiving a new recipe
    :param recipe_id: The recipe being added
    :return:
    """
    insert_sql = "INSERT INTO categories (recipe_id, name) VALUES (%d, %s)"
    exec_commit(insert_sql, [recipe_id, name])

def deleteREcipe(recipe_id, name):
    """
    Removes a recipe from a category
    :param recipe_id: The recipe to be removed
    :param name: The category being used
    :return:
    """
    exec_commit('DELETE FROM categories WHERE recipe_id = %d AND name = %s', [recipe_id, name])

def listCategories():
    """
    Gets all the categories from the category table
    :return: A tuple containing all category names
    """
    exec_get_all('SELECT name FROM categories')

def uniqueCategory(name) -> bool:
    """
    Checks if the category name is unique
    :param name: The name of the category being checked
    :return:
    """

    categories = listCategories()
    for category in categories[0]:
        if category[0] == name:
            return False
    return True

