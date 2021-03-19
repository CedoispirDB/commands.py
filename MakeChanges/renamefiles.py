import glob
import os
from random import randint


def randomName():
    x = 0
    name = ""
    while x < 6:
        name = name + str(randint(0, 9))
        x += 1
    return name


choice = input("Choose a file: ")

for files in glob.glob(os.path.join(choice, '*')):
    print(files)
    path = os.path.split(files)[0]
    ex = os.path.splitext(files)[1]
    os.rename(os.path.splitext(files)[0] + os.path.splitext(files)[1], path + "/m" + randomName() + ex)
