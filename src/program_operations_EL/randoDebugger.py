# TODO get rid of this eventually
"""
This file serves as an easy way to fix issues in the database
Problem 1, null ratings in database from data inputted via spreadsheet
"""
from src.program_operations.recipeOperations import *
from src.db.ingredientsCRUD import *

def debuggg1():
    # reset all ratings to 0
    defaultRating = 0
    get_sql = "SELECT recipe_id FROM recipes WHERE rating IS NULL"
    recipeTups = exec_get_all(get_sql, [])
    for rec in recipeTups:
        updateRecipeRating(rec[0], defaultRating)

def debuggg2():
    updateRecipeRating(517, 2.5)

def debuggggg3():
    breaks = True
    while breaks:
        try:
            insertIngredient("bigChungus", "sus")
            breaks = False
            print("not brokey")
        except Exception:
            print("still brokey")

def debug4():
    select_sql = "SELECT DISTINCT recipe_id FROM cooks WHERE NOT recipe_id = %s"
    allIds = exec_get_all(select_sql, ["6969"])
    for rId in allIds:
        idr = rId[0]
        newRating = 0
        allRatings = getRatingsByRecipeCooked(idr)
        if len(allRatings) == 0:
            return
        for rat in allRatings:
            newRating += getRatingByUserRecipe(rat[0], idr)[0]
        newRating /= len(allRatings)
        updateRecipeRating(idr, newRating)

def printUserPercentRepeatedRecipeCreation():
    select_sql = "SELECT DISTINCT username FROM cooks WHERE username IN (SELECT username FROM cooks GROUP BY username HAVING COUNT(recipe_id) > 1)"
    select_sql2 = "SELECT DISTINCT username FROM cooks WHERE NOT recipe_id = %s"
    notDist = exec_get_all(select_sql, [])
    dist = exec_get_all(select_sql2, ["42069"])
    print("Not distinct: " + str(len(notDist)))
    print("Distinct: " + str(len(dist)))
    for entry in notDist:
        print(entry)

printUserPercentRepeatedRecipeCreation()