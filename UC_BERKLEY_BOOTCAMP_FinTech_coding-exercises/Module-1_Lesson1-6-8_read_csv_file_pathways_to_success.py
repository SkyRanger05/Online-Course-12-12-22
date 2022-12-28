"""Pathways to Success."""
# @TODO: Import the Path tool from the pathlib library
# YOUR CODE HERE!
import csv
from pathlib import Path

# @TODO: Create a path to the `quarterly_data.csv` file
# YOUR CODE HERE!
my_directory = Path('.')
qrt_path = Path("quarterly_data_copy.csv")
#with open(csvpath) as csvfile:
with open(qrt_path) as q_q:
    qrt_data = csv.reader(q_q)
    counter = 0
    for row in qrt_data: # Iterable object
        counter = counter + 1 
        print(f"Row counter: {counter}")
        print(row)
# Print the relative path (the relative location of the file)
print(my_directory)
print(f"The relative CSV path is: {qrt_path}")

# Print the absolute path (The absolute location of the file on the computer)
print(f"The absolute CSV path is: {qrt_path.absolute()}")


    

