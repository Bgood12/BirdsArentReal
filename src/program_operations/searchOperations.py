from src.db.categoriesCRUD import *
from src.db.recipesCRUD import *
from src.db.incorporationCRUD import *
from src.db.ingredientsCRUD import *
from src.program_operations.categoriesOperations import *

def searchRecipe(key):
    if key == "categories":
        search = input("Enter name of category: ")
        if uniqueCategory(search, CurrentUser.getUser) == True:
            print("This category does not exist.\n")
            return
        else:
            recipes = listAllInCategory(search, CurrentUser.getUser())
            for recipe in recipes:
                print(recipe)
            check = False
            
            while(check == False):
                recipeChoice = input("Please choose a recipe by name: ")
                for recipe in recipes:
                    if recipeChoice == recipe:
                        check = True;
                        break;
                    else:
                        check = False;
                if check ==False:
                    print("Recipe not in category list")
                    
            result = getRecipesByName(recipeChoice)
            print(result)

    elif key == "name":
        search = input("Enter name of recipe: ")
        result = getRecipesByName(search)
        print(result)

    elif key == "ingredients":
        search = input("Enter name of ingredient: ")
        nameToId = getIngredient(search)[1]  # The ingredient_ids
        ingredToRecipe = extract(getIncorporationsByIngredientID(nameToId))  # The recipe_ids
        recipes = []
        extractFirst(getRecipesByID)
        
        for name in ingredToRecipe:
            recipeName = extract(getRecipesById(name))
            recipes.append(recipeName)
        
        for recipe in recipes:
            print(recipe)

        recipeChoice = input ("Please choose a recipe by name: ") 
        result = getRecipesByName(recipeChoice)
        print(result)


def extract(list):
    return [item[0] for item in list]

def extractFirst(list):
    return [item[1] for item in list]






