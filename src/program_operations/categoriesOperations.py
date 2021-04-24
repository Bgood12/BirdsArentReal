from src.db.categoriesCRUD import *
from src.db.belongsCRUD import *
from src.program_operations.accountOperations import *

def createNewCategory(currentUser: CurrentUser, name):
    if currentUser.isLoggedIn():
        createCategory(currentUser.getUser(), name)
        print("Category has been created")
    else:
        print("No user logged in to create a category")

def deleteCategory(username, category_name):
    print(username + " " + category_name)
    deleteAllBelongsByCategory(category_name)
    deleteUserCategory(username, category_name)

def listAllCategories(username):
    cat = listCategoriesByUser(username)
    print(cat)

def addToCategory(recipe_id, category_name, username):
    addRecipeToCategory(recipe_id, category_name, username)

def deleteFromCategory(recipe_id, category_name, username):
    deleteRecipeFromCategory(recipe_id, category_name, username)

def listAllInCategory(category_name, username):
    return listRecipesByCategory(category_name, username)
