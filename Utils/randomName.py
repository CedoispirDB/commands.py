import os
import glob
import random

choice = input("Choose the file: ")
input("DON'T CHANGE IMPORT FILES")
name = ""
if choice == "":
    exit()
for file in glob.glob(os.path.join(choice, '*')):
    name = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(
        random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    base = os.path.splitext(file)[1]
    newName = choice + "/" + name + base
    print("You file new name is: " + newName)
    os.rename(file, newName)
