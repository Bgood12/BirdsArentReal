from src.db.categoriesCRUD import *
from src.db.recipesCRUD import *
from src.db.incorporationCRUD import *
from src.db.ingredientsCRUD import *
from src.program_operations.categoriesOperations import *

def searchRecipe(key, surtType, currentUser):
    if key == "categories" or key == "c":
        search = input("Enter name of category: ")
        if uniqueCategory(search, currentUser.getUser()) == True:
            print("This category does not exist.\n")
            return
        else:
            recipes = listAllInCategory(search, currentUser.getUser())
            if surtType == "date" or surtType == "d":
                recipes.sort(key=lambda x: x[5])
                recipes.reverse()
                print("Id: Name, rating, creationDate")
                for recipe in recipes:
                    rec = getRecipeByID(recipe[0])
                    print(str(rec[0])+": "+rec[1]+", "+str(rec[2])+", "+str(recipe[5]))
            else:
                print("Id: Rating: Name")
                recs = []
                for recipe in recipes:
                    recs.append(getRecipeByID(recipe[0]))
                if surtType == "rating" or surtType == "r":
                    recs.sort(key=lambda x: x[2])
                    recs.reverse()
                else:
                    recs.sort(key=lambda x: x[1])
                for recipe in recs:
                    print(str(recipe[0])+": "+str(recipe[2])+": "+recipe[1])
            """
            check = False
            while(check == False):
                recipeChoice = input("Please choose a recipe by name: ")
                for recipe in recipes:
                    if recipeChoice == recipe:
                        check = True
                        break
                    else:
                        check = False
                if check ==False:
                    print("Recipe not in category list")
                    
            result = getRecipesByName(recipeChoice)
            print(result)
            """
    elif key == "name" or key == "n":
        searchName = input("Enter a substring of your intended recipe: ").lower()
        result = getRecipesLikeName(searchName)
        if surtType == "rating" or surtType == "r":
            result.sort(key=lambda x:x[2])
            result.reverse()
        elif surtType == "date" or surtType == "d":
            result.sort(key=lambda x:x[7])
            result.reverse()
        else:
            result.sort(key=lambda x:x[1])
        if len(result) == 0:
            print("No recipes contain that string")
            return
        print("Id: rating: name, creationDate")
        for recipe in result:
            print(str(recipe[0])+": "+str(recipe[2])+": "+recipe[1]+", "+str(recipe[7]))

    elif key == "ingredients" or key == "i":
        search = input("Enter id of ingredient: ")
        ingredToRecipe = extract(getIncorporationsByIngredientID(search))  # The recipe_ids
        print(ingredToRecipe) # Check recipe ids
        recipes = ()
        # TODO this type of search is hopelessly broken
        for name in ingredToRecipe:
            recipeName = extractFirst(getRecipesByName(name))
            recipes.append(recipeName)
        if surtType == "rating" or surtType == "r":
            recipes.sort(key=lambda x: x[2])
            recipes.reverse()
        elif surtType == "date" or surtType == "d":
            recipes.sort(key=lambda x: x[2])  # TODO make sort by dates
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






