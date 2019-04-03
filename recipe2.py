import requests as req 
from datetime import datetime
import sqlite3



def addRecipe(name, ingredients = "no ingredients set", instructions = " no instructions set", serving_size = " no serving size set", category = "no category set", notes = "no notes set"):
	date_added = str(datetime.now())
	date_modified = str(datetime.now())
	endpoint = sqlite3.connect("RecipeDatabase")
	cursor = endpoint.cursor()
	cursor.execute("INSERT INTO recipeData VALUES (?,?,?,?,?,?,?,?);",[name, ingredients, instructions, serving_size, category, notes, date_added, date_modified])
	cursor.close()
	endpoint.commit()
	endpoint.close()

def deleteRecipe(name):
	endpoint = sqlite3.connect("RecipeDatabase")
	cursor = endpoint.cursor()
	cursor.execute("DELETE FROM recipeData WHERE name=?", (name,) )
	cursor.close()
	endpoint.commit()
	endpoint.close()

def deleteAllRecipes():
	endpoint = sqlite3.connect("RecipeDatabase")
	cursor = endpoint.cursor()
	cursor.execute("DELETE FROM recipeData")
	cursor.close()
	endpoint.commit()
	endpoint.close()

def listRecipes():
	endpoint = sqlite3.connect("RecipeDatabase")
	cursor = endpoint.cursor()
	cursor.execute("SELECT * FROM recipeData")
	recipes = cursor.fetchall()
	for recipe in recipes:
		print(recipe)
	cursor.close()
	endpoint.close()


def listRecipe(name):
	endpoint = sqlite3.connect("RecipeDatabase")
	cursor = endpoint.cursor()
	cursor.execute("SELECT * FROM recipeData WHERE name=?", (name,) )
	recipe = cursor.fetchall()
	print(recipe)
	cursor.close()
	endpoint.close()

def setIngredients(name, new_ing):
	endpoint = sqlite3.connect("RecipeDatabase")
	cursor = endpoint.cursor()
	command = '''UPDATE recipeData
					SET ingredients = ?,
					date_modified = ?
					WHERE name = ?'''

	cursor.execute(command, (new_ing, str(datetime.now()), name))
	cursor.close()
	endpoint.commit()
	endpoint.close()
	
def setInstructions(name, new_ins):
	endpoint = sqlite3.connect("RecipeDatabase")
	cursor = endpoint.cursor()
	command = '''UPDATE recipeData
					SET instructions = ?,
					date_modified = ?
					WHERE name = ?'''

	cursor.execute(command, (new_ins, str(datetime.now()), name))
	cursor.close()
	endpoint.commit()
	endpoint.close()
	
def setServingSize(name, new_ser):
	endpoint = sqlite3.connect("RecipeDatabase")
	cursor = endpoint.cursor()
	command = '''UPDATE recipeData
					SET serving_size = ?,
					date_modified = ?
					WHERE name = ?'''

	cursor.execute(command, (new_ser, str(datetime.now()), name))
	cursor.close()
	endpoint.commit()
	endpoint.close()
	
def setCategory(name, new_cat):
	endpoint = sqlite3.connect("RecipeDatabase")
	cursor = endpoint.cursor()
	command = '''UPDATE recipeData
					SET category = ?,
					date_modified = ?
					WHERE name = ?'''

	cursor.execute(command, (new_cat, str(datetime.now()), name))
	cursor.close()
	endpoint.commit()
	endpoint.close()
	
def setNotes(name, new_not):
	endpoint = sqlite3.connect("RecipeDatabase")
	cursor = endpoint.cursor()
	command = '''UPDATE recipeData
					SET notes = ?,
					date_modified = ?
					WHERE name = ?'''

	cursor.execute(command, (new_not, str(datetime.now()), name))
	cursor.close()
	endpoint.commit()
	endpoint.close()
	
	
#ingredients
#instructions
#serving size
#category
#notes
#date added
#date modified
