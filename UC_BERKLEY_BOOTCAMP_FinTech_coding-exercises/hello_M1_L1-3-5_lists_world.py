# -*- coding: utf-8 -*-
"""Instructor Demo: Lists.
" all rights reserved "
This script showcases basic operations of Python Lists.
"""
# Title
print("Grand Mama's Apple Pie Recipe")
# 1) make a Lists of ingredients and measurements
dry_ingredients = ["apples", "flour", "cinnamon", "sugar", "baking soda"]
wet_ingredients = ["milk", "eggs", "water", "oil", "vanilla"]
measurements = []
# 2) indexing: retrieving items from the list. index syntax--new_var_name = value
ingredient_1 = dry_ingredients[0]
ingredient_2 = dry_ingredients[1]
ingredient_3 = dry_ingredients[2]
ingredient_4 = dry_ingredients[3]
ingredient_5 = dry_ingredients[4]
print(f"Ingredient 1: {ingredient_1}")
print(f"Ingredient 2: {ingredient_2}")
print(f"Ingredient 3: {ingredient_3}")
print(f"Ingredient 4: {ingredient_4}")
print(f"Ingredient 5: {ingredient_5}")

# 3) add items to a list: list_name[] empty, list_name.append
flour_cups = measurements.append("Flour 4 cups")
flour = measurements[0]
print(flour)
# 4) slicing the list: retrieving subset of the list s:ss, s:_, _:ss
dry = dry_ingredients[:]
wet = wet_ingredients[:]
print(f"Dry ingredients are: {dry_ingredients}")
print(f"Wet ingredients are: {wet}")
# 5) Operations: 
number_of_dry_ingredients = len(dry_ingredients)
print(f"Number of ingredients: {number_of_dry_ingredients} dry ingredients")