# Variables

# This is a comment - any code commented out is not run -
# meaning that any code or text commented out is ignored.

"""
This is a multi-line comment.
You can comment out many lines at once.
For the most part you will see single line comments
As in single line comments, any code contained within multi-line comments is not run -
meaning that any code commented out is ignored.
"""

# Topic: Strings

# Create a variable named `subject` with no value (None).
print()
subject = ""
print(subject)
print()

# Assign a value of "Programmers to the variable `subject`.
print()
subject = "Programmers"
print(subject)
print()

# Create a variable, `first_name`, and assign it a value of an empty string.
print()
first_name = ""
print(first_name)
print()

# Assign a value of "Ada" to the variable `first_name`.
print()
first_name = "Ada"
print(first_name)
print()

# Create a variable, `last_name`, and assign it a value of a string, "Lovelace".
print()
last_name = "Lovelace"
print(last_name)
print()



# Topic: Integers

# Create a variable, `birth_year`, and assign it with an integer of 1815.
print()
birth_year = 1815
print(birth_year)
print()

# Create a variable, death_year, and assign it with an integer of 1852.
print()
death_year = 1852
print(death_year)
print()

# Create a variable, age_at_passing, and assign it a value of death_year minus birth_year.
print()
age_at_passing = death_year - birth_year
print(age_at_passing)
print()


#Topic: Print

# Print: "First Name: " and `first_name`.
print("First Name:", first_name)

# Print: "Last Name: " and `last_name`.
print("Last Name:", last_name)


#Topic: Concat Values

# Create and print a variable, `statement_one`, by assigning it a value of a string:
# "Programmers: Ada Lovelace was born in 1815, and she lived to be 37 years old."
print()
statement_one =  f"{subject}: {first_name} {last_name} was born {birth_year}, and she lived to be {death_year - birth_year} years old."
print(statement_one)
print()
