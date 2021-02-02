from alphabetiz import listOfAnime


def moveAnimes(initialPos, finalPos):
    animeW = listOfAnime(1)
    animeNF = listOfAnime(2)
    animeNS = listOfAnime(3)

    animeToChange = input("What anime would you like to change? ")
    initialPosition = initialPos
    finalPosition = finalPos

    toMove = ""
    if initialPosition == 1:
        toMove = animeW[int(animeToChange) - 1]
        animeW.remove(toMove)
    elif initialPosition == 2:
        toMove = animeNF[int(animeToChange) - 1]
        animeNF.remove(toMove)
    elif initialPosition == 3:
        toMove = animeNS[int(animeToChange) - 1]
        animeNS.remove(toMove)

    if finalPosition == 1:
        if not animeW.__contains__(toMove):
            animeW.append(toMove)
        else:
            print("This anime is already in watched")
    elif finalPosition == 2:
        if not animeNF.__contains__(toMove):
            animeNF.append(toMove)
        else:
            print("This anime is already in not finished")
    elif finalPosition == 3:
        if not animeNS.__contains__(toMove):
            animeNS.append(toMove)
        else:
            print("This anime is already in not started")

    animeW.sort()
    animeNF.sort()
    animeNS.sort()

    return animeW, animeNF, animeNS
