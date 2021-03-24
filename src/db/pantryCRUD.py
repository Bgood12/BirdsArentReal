from src.db.db_utils import *


def insertToPantry(purchace_date, username, ingredient_id, quantity):
    expiration_date = purchace_date + 4  # TODO add expiration date derivation logic
    insert_sql = 'INSERT INTO pantry (purchace_date, username, ingredient_id, expiration_date current_quantity, quantity_bought) VALUES (%s, %s, %d, %s, %d, %d)'
    exec_commit(insert_sql, [purchace_date, username, ingredient_id, expiration_date, quantity, quantity])


def deleteFromPantry(purchace_date, username, ingredient_id):
    exec_commit('DELETE FROM pantry WHERE purchace_date = %s AND username = %s AND ingredient_id = %d', [purchace_date, username, ingredient_id])


def editPantry(purchace_date, username, ingredient_id, expiration_date, current_quantity, quantity_bought):
    update_sql = 'UPDATE pantry SET purchace_date = %s, username = %s, ingredient_id = %d, expiration_date = %s, current_quantity = %d, quantity_bought = %d' \
                 'WHERE purchace_date = %s AND username = %s AND ingredient_id = %d'
    exec_commit(update_sql, [purchace_date, username, ingredient_id, expiration_date, current_quantity, quantity_bought, purchace_date, username, ingredient_id])

