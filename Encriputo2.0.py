import glob
import os
import hashlib
from password import password




while True:
    pw = input("Password: ")
    if password(pw):
        choice = "/Users/youKnow"
        break
    elif pw == "":
        break
    else:
        print("Invalid Password")

if pw == "":
    choice = input("Choose a file: ")

toBytes = False
allowedEx = [".png", ".jpg", ".mp4", ".mp3",".jpeg"]
leave = False

for files in glob.glob(os.path.join(choice, '*')):
    for e in allowedEx:
        if os.path.splitext(files)[1] == e:
            toBytes = True
            leave = True
            break
    if leave:
        break

if toBytes:
    for files in glob.glob(os.path.join(choice, '*')):
        with open(files, "rb") as j:
            img = bytearray(j.read())
            x = os.path.splitext(files)[1]
            if x not in allowedEx:
                print(x + " is not in the system")
                print("Please update the array")
            ex = hashlib.sha1(x.encode()).hexdigest()
            base = os.path.splitext(files)[0]
            new_file = open(base + "." + ex + ".txt", "wb")
            new_file_bytes = bytearray(img)
            new_file.write(new_file_bytes)
            os.remove(files)
else:
    for files in glob.glob(os.path.join(choice, '*')):
        for x in allowedEx:
            ex = hashlib.sha1(x.encode()).hexdigest()
            if files.__contains__(ex):
                base = os.path.splitext(files)[0]
                newB = ""
                for letters in base:
                    if letters != ".":
                        newB = newB + letters
                    else:
                        break

                os.rename(files, newB + x)
