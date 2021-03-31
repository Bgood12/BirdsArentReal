from src.db.categoriesCRUD import *
from src.program_operations.accountOperations import *

def createCategory(currentUser: CurrentUser, recipe_id, name):
    if currentUser.isLoggedIn():
        x = createCategory(recipe_id, name)[1]
        print(x, "category has been created")
    else:
        print("No user logged in to create a category")

def addNewRecipe(recipe_id, name):
    addRecipe(recipe_id, name)

def deleteOldRecipe(recipe_id, name):
    deleteRecipe(recipe_id, name)

def changeCategoryName(name, new_name):
    updateCategory(name, new_name)

def listAllCategories():
    cat = listCategories()
    print(cat)

def listAllRecipes(name):
    recipes = listRecipes(name)
    print(recipes)

