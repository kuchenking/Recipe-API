import requests as req 
from datetime import datetime

endpoint #this is the part where the url is

def addRecipe(name, date_added, date_modified, ingredients = "no ingredients set", instructions = " no instructions set", serving_size = " no serving size set", 
	category = "no category set", notes = "no notes set", )
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
	resnum = r.status_code
	if(resnum >= 400)
		print("Error")
	if(resnum >= 300)
		#something here, what is a redirect anyway
		print("page moved")
	if(resnum >=200)
		print("Success")

def deleteRecipe(name)
	r = req.delete(endpoint, name)

def listRecipies()
	r = req.get(endpoint, )#i dont know what goes here, never used get before

def setIngredients(name, new_ing)
	r = req.put(endpoing, params = {"name":name, "ingredients":new_ing, "date_modified":str(datetime.now())})

def setInstructions(name, new_ins)
	r = req.put(endpoing, params = {"name":name, "instructions":new_ins, "date_modified":str(datetime.now())})

def setServingSize(name, new_ser)
	r = req.put(endpoing, params = {"name":name, "ingredients":new_ing, "date_modified":str(datetime.now())})

def setCategory(name, new_cat)
	r = req.put(endpoing, params = {"name":name, "category":new_cat, "date_modified":str(datetime.now())})

def setNotes(name, new_not)
	r = req.put(endpoing, params = {"name":name, "notes":new_not, "date_modified":str(datetime.now())})


	
#ingredients
#instructions
#serving size
#category
#notes
#date added
#date modified



	



