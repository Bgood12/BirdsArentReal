# TODO get rid of this eventually
"""
This file serves as an easy way to fix issues in the database
Problem 1, null ratings in database from data inputted via spreadsheet
"""
from src.program_operations.recipeOperations import *


def debuggg1():
    # reset all ratings to 0
    defaultRating = 0
    get_sql = "SELECT recipe_id FROM recipes WHERE rating IS NULL"
    recipeTups = exec_get_all(get_sql, [])
    for rec in recipeTups:
        updateRecipeRating(rec[0], defaultRating)

def debuggg2():
    updateRecipeRating(517, 2.5)

debuggg2()