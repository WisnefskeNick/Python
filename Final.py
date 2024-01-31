# Nicholas Wisnefske
# CS 125
# 5/1/2023

import sqlite3

conn = sqlite3.connect('recipes.db') #connects the code to a datbase called recipes
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS recipes
             (name text, ingredients text, steps text)''') # Creates the table if it doesn't exist

while True:
    name = input("Enter the name of the recipe (or 'quit' to exit): ") # Ask for the name of the recipe
    if name.lower() == 'quit': #if the user inputs quit the code will skip to the end
        break

    ingredients = [] #creates and Array for ingredients
    while True:
        ingredient = input("Enter an ingredient (or 'done' when finished): ") # Ask for the ingredients of the recipe
        if ingredient.lower() == 'done': # when user enters done when they are done entering ingredients
            break
        ingredients.append(ingredient) # adds all of the inputs to ingerdients array

    steps = [] #Creates and array for the steps
    while True:
        step = input("Enter a step (or 'done' when finished): ") # Ask for the steps of the recipe
        if step.lower() == 'done': #When user enters done the loop breaks and continues to the next step.
            break
        steps.append(step) # adds all of the inputs to steps array

    c.execute("INSERT INTO recipes VALUES (?, ?, ?)", (name, ', '.join(ingredients), ', '.join(steps))) # Inserts the recipe into the database
    conn.commit()

print("\nAll recipes:") # Prints all the recipes in the database
for row in c.execute("SELECT * FROM recipes"):
    print(row)

conn.close() # Closes the database connection
