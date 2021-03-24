from src.db.db_utils import *
import datetime


def insertToPantry(purchase_date, username, ingredient_id, quantity):
    expiration_date = purchase_date + 4  # TODO add expiration date derivation logic
    insert_sql = 'INSERT INTO pantry (purchase_date, username, ingredient_id, expiration_date current_quantity, ' \
                 'quantity_bought) VALUES (%s, %s, %d, %s, %d, %d) '
    exec_commit(insert_sql, [purchase_date, username, ingredient_id, expiration_date, quantity, quantity])


def deleteFromPantry(purchase_date, username, ingredient_id):
    exec_commit('DELETE FROM pantry WHERE purchase_date = %s AND username = %s AND ingredient_id = %d', [purchase_date, username, ingredient_id])


def editPantry(purchase_date, username, ingredient_id, expiration_date, current_quantity, quantity_bought):
    update_sql = 'UPDATE pantry SET purchase_date = %s, username = %s, ingredient_id = %d, expiration_date = %s, ' \
                 'current_quantity = %d, quantity_bought = %d WHERE purchase_date = %s AND username = %s AND ' \
                 'ingredient_id = %d '
    exec_commit(update_sql, [purchase_date, username, ingredient_id, expiration_date, current_quantity, quantity_bought, purchase_date, username, ingredient_id])


def useIngredientFromPantry(purchase_date, username, ingredient_id, quantity_used):
    update_sql = 'UPDATE pantry SET current_quantity = current_quantity - %d WHERE purchase_date = %s AND username = ' \
                 '%s AND ingredient_id = %d '
    exec_commit(update_sql, [quantity_used, purchase_date, username, ingredient_id])


def getPantryEntry(purchase_date, username, ingredient_id):
    select_sql = 'SELECT * FROM pantry WHERE purchase_date = %s AND username = %s AND ingredient_id = %d'
    return exec_get_one(select_sql, [purchase_date, username, ingredient_id])


def getPantryByUser(username):
    select_sql = 'SELECT * FROM pantry WHERE username = %s'
    return exec_get_all(select_sql, [username])