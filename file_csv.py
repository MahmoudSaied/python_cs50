'''
# reading the csv file and separating its values by comma
with open("students.csv", "r") as file:
    for row in file:
        name = row.rstrip().split(",")
        print(f"{name[0]} is leading the {name[1]} squad")

# doing the same but instead of list we used two variables
with open("students.csv", "r") as file:
    for row in file:
        name, squad = row.rstrip().split(",")
        print(f"{name} is leading the {squad} squad") 

        

# saving the data in a dictionary
structure = []
with open("students.csv", "r") as file:
    for row in file:
        name, squad = row.rstrip().split(",")
        squad_dic = {}
        squad_dic["name"] = name
        squad_dic["squad"] = squad
        # or simpler squad_dic = {"name": name, "squad": squad}
        structure.append(squad_dic)

# defining function to return the key that you want to use
def get_squad(structure):
    return structure["squad"]

# use the function before to sort on it
for row in sorted(structure, key=get_squad, reverse=True):
    print(f"{row['name']} is leading the {row['squad']} squad")

# same as before but using Lambda instead of creating function then call it
for row in sorted(structure, key=lambda structure: structure["squad"]):
    print(f"{row['name']} is leading the {row['squad']} squad")

    '''

import csv

# using reader function in the csv module to read data & add it to a list
structure = []
'''
with open("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        structure.append({"name": row[0], "squad": row[1]})

for row in sorted(structure, key=lambda structure: structure["name"], reverse=True):
    print(f"{row['name']} is leading the {row['squad']} squad")

'''

# using Dictreader fucntion to read the data & add it into dictionary
with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        structure.append({"name": row["name"], "squad": row["squad"]})

for row in sorted(structure, key=lambda structure: structure["name"]):
    print(f"{row['name']} is leading the {row['squad']} squad")


# using Dictreader function to write the data & add it to the csv file
name = input("Write the name of thenew squad lead: ")
squad = input("Write the name of the new squad created: ")
with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "squad"])
    writer.writerow({"name": name, "squad": squad})