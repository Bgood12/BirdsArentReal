from src.db.db_utils import *


def insertIngedient(id, name, aisle):
    insert_sql = 'INSERT INTO ingredients (ingredient_id, ingredient_name, aisle) VALUES (%d, %s, %s)'
    exec_commit(insert_sql, [id, name, aisle])


def deleteIngredient(id):
    exec_commit('DELETE FROM ingredients WHERE ingredient_id = %d', [id])


def editIngrdient(id, name, aisle):
    deleteIngredient(id)
    insertIngedient(id, name, aisle)


def getIngredient(id):
    exec_get_one('SELECT * FROm ingredients WHERE ingredient_id = %d', [id])


