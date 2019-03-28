import requests as req 
from datetime import datetime

endpoint #this is the part where the url is

def addRecipe(name, ingredients = "no ingredients set", instructions = " no instructions set", serving_size = " no serving size set", 
	category = "no category set", notes = "no notes set")
	currentRecipe = {}
	currentRecipe["name"]=name
	currentRecipe["ingredients"] = ingredients
	currentRecipe["instructions"] = instructions
	currentRecipe["serving_size"] = serving_size
	currentRecipe["category"] = category
	currentRecipe["notes"] = notes
	currentRecipe["date_added"] = str(datetime.now())
	currentRecipe["date_modified"] = str(datetime.now())
	r = req.post(endpoint, params = currentRecipe)
	checkCode(r)

def deleteRecipe(name)
	r = req.delete(endpoint, {"name":name})
	checkCode(r)

def listRecipes()
	r = req.get(endpoint)
	checkCode(r)

def listRecipes(name)
	r = req.get(endpoint, {"name":name})
	checkCode(r)

def setIngredients(name, new_ing)
	r = req.put(endpoing, params = {"name":name, "ingredients":new_ing, "date_modified":str(datetime.now())})
	checkCode(r)
	
def setInstructions(name, new_ins)
	r = req.put(endpoing, params = {"name":name, "instructions":new_ins, "date_modified":str(datetime.now())})
	checkCode(r)
	
def setServingSize(name, new_ser)
	r = req.put(endpoing, params = {"name":name, "ingredients":new_ing, "date_modified":str(datetime.now())})
	checkCode(r)
	
def setCategory(name, new_cat)
	r = req.put(endpoing, params = {"name":name, "category":new_cat, "date_modified":str(datetime.now())})
	checkCode(r)
	
def setNotes(name, new_not)
	r = req.put(endpoing, params = {"name":name, "notes":new_not, "date_modified":str(datetime.now())})
	checkCode(r)
	
def checkCode(code)
	resnum = code.status_code
	if(resnum >= 400)
		print("Error")
	if(resnum >= 300)
		print("page moved")
	if(resnum >=200)
		print("Success")
	
#ingredients
#instructions
#serving size
#category
#notes
#date added
#date modified



	



