import os
import glob
from getExtension import getEx, getName

location = os.getcwd()

for f in glob.glob(os.path.join(location, "*")):
    if os.path.splitext(f)[1] == ".txt":
        ex = "png" 
    else:
        ex = "txt"

for f in glob.glob(os.path.join(location, "*")):
    
    name = os.path.split(f)[0] + "/" + getName(f) + getEx(location, getName(f))

    path = os.path.splitext(name)[0]

    newFile = path + "." + ex

    os.rename(name, newFile)

