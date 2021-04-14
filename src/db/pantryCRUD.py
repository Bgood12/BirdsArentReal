from src.db.db_utils import *
import datetime


def addDays(purchase_date, num_days):
    # add days to a date to make it easier to input expiration dates
    time_change = datetime.timedelta(days=num_days)
    return purchase_date + time_change


def insertToPantry(purchase_date, username, ingredient_id, quantity, expiration_date):
    # insert a new value into the pantry
    insert_sql = 'INSERT INTO pantry (purchase_date, username, ingredient_id, expiration_date, ' \
                 'current_quantity, quantity_bought) VALUES (%s, %s, %s, %s, %s, %s) '
    exec_commit(insert_sql, [purchase_date, username, ingredient_id, expiration_date, quantity, quantity])


def deleteFromPantry(purchase_date, username, ingredient_id):
    # delete an entry from the pantry
    exec_commit('DELETE FROM pantry WHERE purchase_date = %s AND username = %s AND ingredient_id = %s', [purchase_date, username, ingredient_id])


def editPantry(purchase_date, username, ingredient_id, expiration_date, current_quantity, quantity_bought):
    # update all data for a pantry entry. This is mainly for fixing errors in the pantry.
    update_sql = 'UPDATE pantry SET purchase_date = %s, username = %s, ingredient_id = %s, expiration_date = %s, ' \
                 'current_quantity = %s, quantity_bought = %s WHERE purchase_date = %s AND username = %s AND ' \
                 'ingredient_id = %s '
    exec_commit(update_sql, [purchase_date, username, ingredient_id, expiration_date, current_quantity, quantity_bought, purchase_date, username, ingredient_id])


def useIngredientFromPantry(purchase_date, username, ingredient_id, quantity_used):
    # use an amount of a given ingredient
    ingredient = getPantryEntry(purchase_date, username, ingredient_id)
    if quantity_used >= ingredient[4]:
        deleteFromPantry(purchase_date, username, ingredient_id)
        return quantity_used - ingredient[4]
    else:
        update_sql = 'UPDATE pantry SET current_quantity = current_quantity - %s WHERE purchase_date = %s AND username = ' \
                 '%s AND ingredient_id = %s '
        exec_commit(update_sql, [quantity_used, purchase_date, username, ingredient_id])
        return 0


def getPantryEntry(purchase_date, username, ingredient_id):
    # get a tuple entry from the pantry
    select_sql = 'SELECT * FROM pantry WHERE purchase_date = %s AND username = %s AND ingredient_id = %s'
    return exec_get_one(select_sql, [purchase_date, username, ingredient_id])


def getPantryByUser(username):
    # get the entire pantry of a user
    select_sql = 'SELECT * FROM pantry WHERE username = %s'
    return exec_get_all(select_sql, [username])


def getIngredientsByUser(username):
    select_sql = 'SELECT ingredient_id FROM pantry WHERE username = %s'
    return exec_get_all(select_sql, [username])


def getAmountOfIngredient(username, ingredient_id):
    # get the amount of an ingredient in the user's pantry regardless of purchase date
    select_sql = 'SELECT current_quantity FROM pantry WHERE username = %s AND ingredient_id = %s'
    amounts = exec_get_all(select_sql, [username, ingredient_id])
    total_quantity = 0
    for quantity in amounts:
        total_quantity += quantity[0]
    return total_quantity


def useIngredientByClosestExpirationDate(username, ingredient_id, quantity):
    select_sql = 'SELECT * FROM pantry WHERE username = %s AND ingredient_id = %s'
    entries = exec_get_all(select_sql, [username, ingredient_id])
    entries.sort(key=lambda x:x[3]) # should sort by expiration date
    i = 0
    while quantity > 0:
        entry = entries[i]
        quantity = useIngredientFromPantry(entry[0], username, ingredient_id, quantity)
