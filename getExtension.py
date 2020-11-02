import os
import glob


def lettersInName(x, k, count):
    e = x[0:-1]
    newString = e
    c = count + 1
    if k == "/":
        return count + 1
    else:
        k = e[-2:-1]

    return lettersInName(newString, k, c)


# Get a name of a file given its path
def getName(path):
    path = os.path.splitext(path)[0]
    return path[-lettersInName(path, "", 0):]


# Get a file extensions given its name
def getEx(path, name):
    for files in glob.glob(os.path.join(path, "*")):
        if getName(files) == name:
            return os.path.splitext(files)[1]


