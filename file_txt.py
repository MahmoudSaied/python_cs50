x = input("Write you name? ")

# Opening file and write some data in it - you have to close the file
file = open("names.txt", "a")
file.write(f"{x}\n")
file.close()


# Doing the same but using "with" 
with open("names.txt", "a") as file:
    file.write(f"{x}\n")


# Read the file 
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print(line)

# Read the file in compact way
with open("names.txt", "r") as file:
    for line in file:
        print(line)



# Sorting the file data into list then work on the list
names = []

with open("names.txt", "r") as file:
    for i in file:
        names.append(i)

for name in sorted(names, reverse=True):
    print(f"Hello {name}")