import glob
import os


def findFile(dir, match):
    for files in glob.glob(os.path.join(dir, '*')):
        if files.__contains__(match):
            print(files)
        if os.path.isdir(files):
            findFile(files, match)


def findGC(dir):
    for files in glob.glob(os.path.join(dir, '*')):
        if files.__contains__("chrome") or files.__contains__("Chrome") or files.__contains__(
                "CHROME") or files.__contains__("Google"):
            print(files)

        if os.path.isdir(files):
            findGC(files)




m = input("Which File would you like? ")
m = m.lower()

d = input("What is the star point? ")
if d == "":
    findFile("/Users/marcoBarreirinhas", m)
else:
    findFile(d, m)
