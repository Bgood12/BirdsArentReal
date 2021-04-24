from src.db.categoriesCRUD import *
from src.db.recipesCRUD import *
from src.db.incorporationCRUD import *
from src.db.ingredientsCRUD import *
from src.program_operations.categoriesOperations import *

def searchRecipe(key, surtType, currentUser):
    if key == "categories":
        search = input("Enter name of category: ")
        if uniqueCategory(search, currentUser.getUser()) == True:
            print("This category does not exist.\n")
            return
        else:
            recipes = listAllInCategory(search, currentUser.getUser())
            if surtType == "rating":
                recipes.sort(key=lambda x: x[2])
                recipes.reverse()
            elif surtType == "date":
                recipes.sort(key=lambda x: x[5])
                recipes.reverse()
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
        searchName = input("Enter a substring of your intended recipe: ").lower()
        result = getRecipesLikeName(searchName)
        if surtType == "rating":
            result.sort(key=lambda x:x[2])
            result.reverse()
        elif surtType == "date":
            result.sort(key=lambda x:x[7])
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
            recipes.reverse()
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






