import glob
import os
import sys

if sys.argv[1] != "1":
    x = int(sys.argv[1]) + 1
else:
    x = 1

screenShoot = []
for files in glob.glob(os.path.join("/Users/marcobarreirinhas1/Desktop/Manga", '*')):
    if not os.path.isdir(files):
        screenShoot.append(files)

screenShoot.sort()

for files in screenShoot:
    path = os.path.split(files)[0]
    ex = os.path.splitext(files)[1]
    os.rename(os.path.splitext(files)[0] + os.path.splitext(files)[1], path + "/page" + str(x) + ex)
    x += 1
