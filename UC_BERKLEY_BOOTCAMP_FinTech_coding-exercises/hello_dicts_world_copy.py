# -*- coding: utf-8 -*-
"""Instructor Demo: Dictionaries

This script showcases basic operations of Python Dicts.
"""

# Initialize a dictionary containing top traders for each month in 2019
top_traders_2019 = {
    "February": "Samantha",
    "March": "Jordan",
    "April": "May",
    "May": "Rick",
    "June": "Rosie",
    "July": "Emmanuel",
    
}

# Initialize a dictionary



# Print out dictionary, initial print() to serve as spacing between command line input
print()
print(top_traders_2019)
print()

# Print out specific value of a key
print()
print(top_traders_2019["June"])
print(top_traders_2019["March"])
print()

# Add a new key-value pair
print()
top_traders_2019["January"] = "Christian"
top_traders_2019["August"] = "Nguyen"
print(top_traders_2019)
print()

# Modify a key value
print()
top_traders_2019["May"] = "Mario Lopez"
top_traders_2019["April"] = "Jasmine"
print(top_traders_2019)
print()

# Access a the value of a key using the get() method
print()
var = top_traders_2019.get("February")
print(var)
print()

# Delete a key-value pair
print()
del top_traders_2019["May"]
print(top_traders_2019)
print()