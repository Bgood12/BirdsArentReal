from src.db.recipesCRUD import *
from src.db.authorshipCRUD import *
from src.program_operations.accountOperations import *

def topFifty():
    return exec_get_all("SELECT * FROM recipes ORDER BY rating DESC LIMIT 50")
