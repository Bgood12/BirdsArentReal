from src.db.db_utils import *


def insertIngredient(name, aisle):
    insert_sql = 'INSERT INTO ingredients (ingredient_name, aisle) VALUES (%s, %s)'
    exec_commit(insert_sql, [name, aisle])


def deleteIngredient(id):
    exec_commit('DELETE FROM ingredients WHERE ingredient_id = %d', [id])


def editName(id, name):
    update_sql = 'UPDATE ingredients SET ingredient_name = %s WHERE ingredient_id = %d'
    exec_commit(update_sql, [name, id])


def editAisle(id, aisle):
    update_sql = 'UPDATE ingredients SET aisle = %s WHERE ingredient_id = %d'
    exec_commit(update_sql, [aisle, id])


def editIngredient(id, name, aisle):
    update_sql = 'UPDATE ingredients SET ingredient_name = %s, aisle = %s WHERE ingredient_id = %d'
    exec_commit(update_sql, [name, aisle, id])


def getIngredient(id):
    return exec_get_one('SELECT * FROm ingredients WHERE ingredient_id = %d', [id])


