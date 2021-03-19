import sys
from Utils.utils import isText
from Utils.utils import locate

animePos = 0
initPos = 0
finPos = 0

watched = []
notFinished = []
notStarted = []
manga = []
links = []

x = 0
count = 1
aList = 0
showContent = False
move = False
addAnime = False
find = False
givePos = False
newAnime = ""
change = ""
search = ""

# Show anime variables
w = False
nf = False
ns = False
m = False
countW = False

# Count number os animes variables
countF = False
countS = False
countM = False
countTotal = False

if len(sys.argv) > 1:
    arg = sys.argv[1]
    if arg.__contains__("show"):
        showContent = True
        if len(arg) > 4 and int(arg[arg.index("w") + 1:]) <= 4:
            aList = int(arg[arg.index("w") + 1:])
        elif len(arg) > 4:
            print(str(int(arg[arg.index("w") + 1:])) + " is not a list")
            exit()
    elif arg.__contains__("total"):
        countTotal = True
        if arg[len(arg) - 1:] == "1":
            countW = True
        elif arg[len(arg) - 1:] == "2":
            countF = True
        elif arg[len(arg) - 1:] == "3":
            countS = True
        elif arg[len(arg) - 1:] == "4":
            countM = True
    elif arg[len(arg) - 1:] == "f":
        find = True
        search = arg[:len(arg) - 1]
    elif arg[len(arg) - 1:] == "p":
        givePos = True
        find = True
        search = arg[:len(arg) - 1]
    elif arg == "h":
        print("To organize an anime:\nrun the program without any arguments\n")
        print(
            "To Move an anime:\nType the position of the anime you want to move, the number of the list that this "
            "anime is, "
            " and the number of the list this anime should go(without any space between them)\n")
        print(
            "To add an anime:\nType the name of the anime e put the number of the list in the end of the name("
            "without any space)\n*If the name has more than one word, put it between quotes*\n")
        print(
            "To find an anime:\nType the name of the anime you would like and add and 'f' in the end(without any "
            "space)\n")
        print("To show how many in which a certain list:\nWrite \"total\" + 1/2/3(from which list you want)\n")
        print(
            "To show the list of animes:\nType \"show\", if you want an specific list type type \"show\"  + "
            "1/2/3(from which list you want)")
        exit(0)
    elif isText(arg):
        addAnime = True
        newAnime = arg[:len(arg) - 1]
        finPos = int(arg[len(arg) - 1:])
    elif len(arg) >= 3:
        animePos = int(arg[0: len(arg) - 2]) - 1
        initPos = int(arg[len(arg) - 2])
        finPos = int(arg[len(arg) - 1])
        move = True
    else:
        print("Invalid argument(Require 3 digits)")
        exit(0)

# Open files to read from and to write on
file = open("/Users/marcobarreirinhas1/Programs/Python/UtilsTexts/AnimeList.txt", "r")
file2 = open("/Users/marcobarreirinhas1/Programs/Python/UtilsTexts/AnimeList2.txt", "w")

for line in file:
    line = line.strip("\n")

    if line.__contains__("Watched") or line.__contains__("Not Finished") or line.__contains__(
            "Not Started") or line.__contains__("Links") or line.__contains__("Manga"):
        x += 1
    if line.__contains__(")"):
        if not (line.__contains__("Watched") or line.__contains__("Not Finished") or line.__contains__(
                "Not Started") or line.__contains__("Manga")):
            if x == 1:
                watched.append(line[line.index(")") + 2:])
            elif x == 2:
                notFinished.append(line[line.index(")") + 2:])
            elif x == 3:
                notStarted.append(line[line.index(")") + 2:])
            elif x == 4:
                manga.append(line[line.index(")") + 2:])
    elif x == 5:
        links.append(line)

# Find an anime in any of the lists
if find:
    k = locate(search, watched, notFinished, notStarted)
    pos = k[0]
    List = k[1]
    if givePos:
        pos = str(pos + 1) + str(List)
        sys.exit(pos)
    else:
        pass

    if List == 1:
        print(watched[pos] + " was found in watched, position " + str(pos + 1))
    if List == 2:
        print(notFinished[pos] + " was found in not finished, position " + str(pos + 1))
    if List == 3:
        print(notStarted[pos] + " was found in not started, position " + str(pos + 1))
    exit()

# Move an anime from a list to another
if move:
    if initPos == 1:
        change = watched[animePos]
        watched.remove(change)
    elif initPos == 2:
        change = notFinished[animePos]
        notFinished.remove(change)
    elif initPos == 3:
        change = notStarted[animePos]
        notStarted.remove(change)
    else:
        print("There is no other list")
    if finPos == 1:
        if not watched.__contains__(change):
            watched.append(change)
        else:
            print("This anime is already in this list")
    elif finPos == 2:
        if not notFinished.__contains__(change):
            notFinished.append(change)
        else:
            print("This anime is already in this list")
    elif finPos == 3:
        if not notStarted.__contains__(change):
            notStarted.append(change)
        else:
            print("This anime is already in this list")
    print("The Anime \"" + change + "\" was removed from list " + str(initPos) + " and added to list " + str(finPos))

# Add new anime
if addAnime:
    if finPos == 1:
        if not watched.__contains__(newAnime):
            watched.append(newAnime)
            print(newAnime + " was added to the watched list")
        else:
            print("This anime is already in this list. In position: " + str(watched.index(newAnime) + 1))
    elif finPos == 2:
        if not notFinished.__contains__(newAnime):
            notFinished.append(newAnime)
            print(newAnime + " was added to the not finished list")
        else:
            print("This anime is already in this list. In position: " + str(notFinished.index(newAnime) + 1))
    elif finPos == 3:
        if not notStarted.__contains__(newAnime):
            notStarted.append(newAnime)
            print(newAnime + " was added to the not started list")
        else:
            print("This anime is already in this list. In position: " + str(notStarted.index(newAnime) + 1))
    elif finPos == 4:
        if not manga.__contains__(newAnime):
            manga.append(newAnime)
            print(newAnime + " was added to the manga list")
        else:
            print("This manga is already in this list. In position: " + str(manga.index(newAnime) + 1))

# Show number of Animes in each list
if countTotal:
    if not (countW or countF or countS):
        print("Total: " + str(len(watched) + len(notFinished) + len(notStarted)))
    if countW:
        print("Animes watched: " + str(len(watched)))
    elif countF:
        print("Animes not finished: " + str(len(notFinished)))
    elif countS:
        print("Animes not started: " + str(len(notStarted)))
    elif countM:
        print("Mangas: " + str(len(manga)))
    exit()

# Sort list alphabetically
watched.sort()
notFinished.sort()
notStarted.sort()
manga.sort()
links.sort()

# Write in the file
if not showContent:
    file2.write("Anime\n\n\n")

    file2.write("Watched/In Progress(" + str(len(watched)) + "):\n\n")
    for n in watched:
        file2.write(str(count) + ") " + n + "\n")
        count += 1
    count = 1

    file2.write("\n\nNot Finished(" + str(len(notFinished)) + "):\n\n")
    for n in notFinished:
        file2.write(str(count) + ") " + n + "\n")
        count += 1
    count = 1

    file2.write("\n\nNot Started(" + str(len(notStarted)) + "):\n\n")
    for n in notStarted:
        file2.write(str(count) + ") " + n + "\n")
        count += 1
    count = 1
    file2.write("\n\nManga/Manhwa(" + str(len(manga)) + "):\n\n")
    for n in manga:
        file2.write(str(count) + ") " + n + "\n")
        count += 1

    file2.write("\n\n")
    file2.write("Animes watched: " + str(len(watched)))
    file2.write("\nAnimes not finished: " + str(len(notFinished)))
    file2.write("\nAnimes not started: " + str(len(notStarted)))
    file2.write("\nTotal number of Animes: " + str(len(watched) + len(notFinished) + len(notStarted)) + "\n\n")
    for n in links:
        file2.write(n + "\n")

    file.close()
    file2.close()
    file = open("/Users/marcobarreirinhas1/Programs/Python/UtilsTexts/AnimeList.txt", "w")
    file2 = open("/Users/marcobarreirinhas1/Programs/Python/UtilsTexts/AnimeList2.txt", "r")
    for k in file2:
        file.write(k)
else:
    if aList == 1:
        w = True
    elif aList == 2:
        nf = True
    elif aList == 3:
        ns = True
    elif aList == 4:
        m = True
    else:
        w = True
        nf = True
        ns = True
        m = True

    if w:
        print("List #1(watched):")
        count = 1
        for n in watched:
            print(str(count) + ") " + n)
            count += 1
        count = 1
        print("")
    if nf:
        print("List #2(not finished):")
        for n in notFinished:
            print(str(count) + ") " + n)
            count += 1
        count = 1
        print("")
    if ns:
        print("List #3(not started):")
        for n in notStarted:
            print(str(count) + ") " + n)
            count += 1
        count = 1
        print("")
    if m:
        print("List #4(manga):")
        for n in manga:
            print(str(count) + ") " + n)
            count += 1
