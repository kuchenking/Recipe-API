import sqlite3

recipeDatabase = 'RecipeDatabase'    # name of the sqlite database file
recipeData = 'RecipeData'  # name of the table to be created
#ingredients
#instructions
#serving size
#category
#notes
#date added
#date modified

# Connecting to the database file
conn = sqlite3.connect(recipeDatabase)
c = conn.cursor()

# Creating a new SQLite table with 1 column
c.execute('CREATE TABLE recipeData (name TEXT)')

#creating new columns
c.execute("ALTER TABLE recipeData ADD COLUMN 'ingredients' TEXT")
       
c.execute("ALTER TABLE recipeData ADD COLUMN 'instructions' TEXT")
       
c.execute("ALTER TABLE recipeData ADD COLUMN 'serving size' TEXT")

c.execute("ALTER TABLE recipeData ADD COLUMN 'category' TEXT")
       
c.execute("ALTER TABLE recipeData ADD COLUMN 'notes' TEXT")

c.execute("ALTER TABLE recipeData ADD COLUMN 'date_added' TEXT")
       
c.execute("ALTER TABLE recipeData ADD COLUMN 'date_modified' TEXT")
        

conn.commit()
conn.close()


    
