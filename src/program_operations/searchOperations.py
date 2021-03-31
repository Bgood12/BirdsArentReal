from src.db.categoriesCRUD import *
from src.db.recipesCRUD import *
from src.db.incorportationCRUD import *
from src.db.ingredientsCRUD import *
from src.program_operations.categoriesOperations import *

def searchRecipe(key):
    if key == "categories":
        search = input("Enter name of category: ")
        if uniqueCategory(search) == True:
            print("This category does not exist.\n")
            return
        else:
            recipes = listAllRecipes(search)
            for recipe in recipes:
                print(recipe)
            recipeChoice = input("Please choose a recipe by name: ")
            result = getRecipesByName(recipeChoice)
            print(result)

    elif key == "name":
        search = input("Enter name of recipe: ")
        result = getRecipesByName(search)
        print(result)

    elif key == "ingredients":
        search = input("Enter name of ingredient: ")
        nameToId = getIngredient(search)[1]  # The ingredient_ids
        ingredToRecipe = extract(getIncorporationByIngredientID(nameToId))  # The recipe_ids

        for recipe in ingredToRecipe:
            print(recipe)

        recipeChoice = input ("Please choose a recipe by ID: ") #till i figure out how to get names instead
        result = getRecipesByID(recipeChoice)
        print(result)


def extract(list):
    return [item[0] for item in list]






