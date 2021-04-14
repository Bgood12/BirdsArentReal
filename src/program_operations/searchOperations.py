from src.db.categoriesCRUD import *
from src.db.recipesCRUD import *
from src.db.incorporationCRUD import *
from src.db.ingredientsCRUD import *
from src.program_operations.categoriesOperations import *

def searchRecipe(key, surtType):
    if key == "categories":
        search = input("Enter name of category: ")
        if uniqueCategory(search, CurrentUser.getUser) == True:
            print("This category does not exist.\n")
            return
        else:
            recipes = listAllInCategory(search, CurrentUser.getUser())
            if surtType == "rating":
                recipes.sort(key=lambda x: x[2])
            elif surtType == "date":
                recipes.sort(key=lambda x: x[2])  # TODO fix
            else:
                recipes.sort(key=lambda x: x[1])
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
        if surtType == "rating":
            result.sort(key=lambda x:x[2])
        elif surtType == "date":
            result.sort(key=lambda x:x[2]) # TODO fix
        else:
            result.sort(key=lambda x:x[1])
        print(result)

    elif key == "ingredients":
        search = input("Enter id of ingredient: ")
        ingredToRecipe = extract(getIncorporationsByIngredientID(search))  # The recipe_ids
        print(ingredToRecipe) # Check recipe ids
        recipes = ()
        
        for name in ingredToRecipe:
            recipeName = extractFirst(getRecipesByName(name))
            recipes.append(recipeName)
        if surtType == "rating":
            recipes.sort(key=lambda x: x[2])
        elif surtType == "date":
            recipes.sort(key=lambda x: x[2])  # TODO fix
        else:
            recipes.sort(key=lambda x: x[1])
        for recipe in recipes:
            print(recipe)

        recipeChoice = input ("Please choose a recipe by name: ") 
        result = getRecipesByName(recipeChoice)
        print(result)


def extract(list):
    return [item[0] for item in list]

def extractFirst(list):
    return [item[1] for item in list]






