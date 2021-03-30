from src.db.recipesCRUD import *
from src.db.authorshipCRUD import *
from src.program_operations.accountOperations import *

def newRecipe(currentUser: CurrentUser, name, description, cooktime, steps, difficulty):
    if currentUser.isLoggedIn():
        id = createRecipe(name, description, cooktime, steps, difficulty)[0] # Get the ID from the returned tuple
        createAuthorship(currentUser.getUser(), id)
        print("Recipe has been created")
    else:
        print("No user logged in to create the recipe")

