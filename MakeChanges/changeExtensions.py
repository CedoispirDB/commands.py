import os
import glob
from Utils.getExtension import getEx, getName

# location = os.getcwd()

q = input("You are going to change the extension of all the files in this folder. Are you sure? ")
q = q.lower()

if q == "n" or q == "no":
    exit()
ex = ""
location = input("Path the folder with the files you want: ")


# for f in glob.glob(os.path.join(location, "*")):
#     if os.path.splitext(f)[1] == ".txt":
#         ex = "png"
#     else:
#         ex = "txt"

for f in glob.glob(os.path.join(location, "*")):
    
    name = os.path.split(f)[0] + "/" + getName(f) + getEx(location, getName(f))

    path = os.path.splitext(name)[0]

    newFile = path + "." + "jpg"

    os.rename(name, newFile)

