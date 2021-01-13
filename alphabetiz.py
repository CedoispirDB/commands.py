def isText(line):
    line = line.lower()
    if line.__contains__("a") or line.__contains__("e") or line.__contains__("i") or line.__contains__(
            "o") or line.__contains__("u"):
        return True
    else:
        return False


def listOfAnime(x):
    animeList = open("/Users/marcobarreirinhas/Programs/Python/AnimeList.txt", "r")
    animeWList = []
    animeNFList = []
    animeNSList = []
    linksList = []

    ok1 = False
    ok2 = False
    ok3 = False
    ok4 = False

    for lines in animeList:

        lines = lines.strip("\n")

        if lines.__contains__("Watched"):
            ok1 = True
        if lines.__contains__("Not finished"):
            ok2 = True
            ok1 = False
        if lines.__contains__("Not started"):
            ok3 = True
            ok2 = False
        if lines.__contains__("Links"):
            ok4 = True
            ok3 = False

        if ok1:
            if not lines.__contains__("Watched"):
                if isText(lines):
                    animeWList.append(lines)
        elif ok2:
            if not lines.__contains__("Not finished"):
                if isText(lines):
                    animeNFList.append(lines)
        elif ok3:
            if not lines.__contains__("Not started"):
                if isText(lines):
                    animeNSList.append(lines)
        elif ok4:
            if not lines.__contains__("Links"):
                if not lines.__contains__("Links"):
                    if isText(lines):
                        linksList.append(lines)

    if x == 1:
        animeWList.sort()
        return animeWList
    elif x == 2:
        animeNFList.sort()
        return animeNFList
    elif x == 3:
        animeNSList.sort()
        return animeNSList
    elif x == 4:
        linksList.sort()
        return linksList
    else:
        return []


def write():
    animeW = listOfAnime(1)
    animeNF = listOfAnime(2)
    animeNS = listOfAnime(3)
    links = listOfAnime(4)

    countW = len(animeW)
    countNF = len(animeNF)
    countNS = len(animeNS)

    animeList2 = open("/Users/marcobarreirinhas/Programs/Python/AnimeList2.txt", "w")

    count = 1

    animeList2.write("Anime\n\n\n")
    animeList2.write("Watched/In progress(" + str(countW) + "):\n")
    for n in animeW:
        animeList2.write("\n")
        animeList2.write(str(count) + ") " + n)
        count += 1

    count = 1
    animeList2.write("\n\n\n")
    animeList2.write("Not Finished(" + str(countNF) + "):\n")
    for n in animeNF:
        animeList2.write("\n")
        animeList2.write(str(count) + ") " + n)
        count += 1
    count = 1
    animeList2.write("\n\n\n")
    animeList2.write("Not Started(" + str(countNS) + "):\n")
    for n in animeNS:
        animeList2.write("\n")
        animeList2.write(str(count) + ") " + n)
        count += 1

    animeList2.write("\n\n\nAnimes watched: " + str(countW))
    animeList2.write("\nAnimes not finished: " + str(countNF))
    animeList2.write("\nAnimes not started: " + str(countNS))
    animeList2.write("\nTotal number of Animes: " + str(countW + countNF + countNS))

    animeList2.write("\n\n")
    animeList2.write("Links:")
    for n in links:
        animeList2.write("\n")
        animeList2.write(n)


write()
