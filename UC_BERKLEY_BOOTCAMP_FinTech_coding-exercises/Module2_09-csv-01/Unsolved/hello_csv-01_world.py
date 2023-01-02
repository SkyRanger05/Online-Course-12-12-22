# Import the necessary libraries for reading csv files
import csv
from pathlib import Path


# Set the path for the csv file
csvpath = Path("pokemon.csv")
print(csvpath)

# Create new lists to store data for heaviest and tallest Pokemon
h_t = []
# Open the csv
with open(csvpath) as p:
    data = csv.reader(p)

    # Iterate through the data and search for the number the user inputted. Remember to skip the header of the CSV.
    for item in data:
        #skip header
        g = item[1]
        r = item[0]
        d = g + r
        h = item[4]
        #if r == "25":
            
        # Print the name of the Pokemon(identifier) and Pokedex number(species id) at that number. For example, "Pokemon No. 25 - Pikachu".
           # print(f"Pokemon No. {r} - {g}. Weight {h}")
        #print(h)
        # Iterate through the data and search for Pokemon whose weight is greater than 3000. Append only the Pokemon's name and weight to the 'heaviest' list.
        if h > "3000":
            h = return()
            #item.append(h_t)
            print(h_t)
        else:
            print("Leight Weight")
        # Iterate through the data and search for Pokemon whose height is greater than 50. Append only the Pokemon's name and height to the 'tallest' list.


# Print the list of heaviest and tallest pokemon
