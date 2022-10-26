import subprocess
import os
# 2021-04-05 18.30.26 Miraculous (Kids - Francês) 92948203158
# path: /Users/marcobarreirinhas1/Documents/Zoom

# delete folder after save
# automatically put on review

folder = subprocess.getstatusoutput('ls /Users/marcobarreirinhas1/Documents/Zoom')


file = open(f"/Users/marcobarreirinhas1/Documents/Zoom/{folder[1]}/meeting_saved_chat.txt", "r")
file2 = open("/Users/marcobarreirinhas1/Desktop/General/Programming/french/edited.txt", "w")

for lines in file:
    if not (lines.__contains__("Beatriz") or lines.__contains__("NATALIA") or lines.__contains__("Marco") or lines.__contains__("Julia")):
        lines = lines.split(":")
        lines = lines[len(lines) - 1]
        if lines[0] == " ":
            file2.write(lines[1:])
            print(lines)
        else:
            file2.write(lines)
            print(lines)

os.system(f"rm -r /Users/marcobarreirinhas1/Documents/Zoom/'{folder[1]}'")