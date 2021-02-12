from spellCheck import checkSimilarity


def checkForSameValues(listM):
    count = 0
    for n in listM:
        for k in range(len(listM)):
            if n == listM[k]:
                count += 1
                if count == 2:
                    print("there is two of "  + n )


def isText(line):
    line = line.lower()
    if line.__contains__("a") or line.__contains__("e") or line.__contains__("i") or line.__contains__(
            "o") or line.__contains__("u"):
        return True
    else:
        return False


def sumLists(list1, list2, list3):
    newList = []
    for n in list1:
        newList.append(n.lower())
    for n in list2:
        newList.append(n.lower())
    for n in list3:
        newList.append(n.lower())
    return newList


def locate(search, list1, list2, list3):
    search = str(search).lower()
    listNumber = 0
    location = 0
    pos = 0
    leave = False
    found = False

    size1 = len(list1)
    size2 = len(list2)
    size3 = len(list3)

    totalList = sumLists(list1, list2, list3)
    if totalList.__contains__(search):
        pos = totalList.index(search)
    else:
        for n in totalList:
            name = n

            if n.__contains__(search):
                pos = totalList.index(name)
                found = True
                break
            n = n.split()
            # print("search: " + str(search.split()))
            # print("n: " + str(n))
            ss = search.split()
            if len(ss) >= 2:
                if ss.__contains__(n[0]) or ss.__contains__(n[1]):
                    pos = totalList.index(name)
                    found = True
                    break
            for k in n:
                if k.__contains__(search):
                    pos = totalList.index(name)
                    leave = True
                    found = True
                    break

            if leave:
                break

    if not found:
        # x = checkSimilarity(search, totalList, 50)
        # response = ""
        # value = ""
        # print(x)
        # for n in range(len(x)):
        #     for k in totalList:
        #         name = k
        #         k = k.split()
        #         # print("x: " + str(x))
        #         # print("k: " + str(k))
        #         checkForSameValues(x)
        #         print(x[n])
        #         print(value)
        #         if k.__contains__(value):
        #             pos = totalList.index(name)
        #             if pos < size1:
        #                 location = list1.index(list1[pos])
        #
        #                 if n == len(x):
        #                     response = response + "\"" + list1[location]
        #                 else:
        #                     response = response + "\"" + list1[location] + "\" or "
        #             elif pos < size1 + size2:
        #                 location = list2.index(list2[pos - size1])
        #                 if n == len(x):
        #                     response = response + "\"" + list2[location]
        #                 else:
        #                     response = response + "\"" + list2[location] + "\" or "
        #             elif pos < size1 + size2 + size3:
        #                 location = list3.index(list3[pos - size1 - size2])
        #                 if n == len(x):
        #                     response = response + "\"" + list3[location]
        #                 else:
        #                     response = response + "\"" + list3[location] + "\" or "
        #             break
        # print("Did you mean " + response)
        print(search + " was not find")
        exit()

    if pos < size1:
        location = list1.index(list1[pos])
        listNumber = 1
    elif pos < size1 + size2:
        location = list2.index(list2[pos - size1])
        listNumber = 2
    elif pos < size1 + size2 + size3:
        location = list3.index(list3[pos - size1 - size2])
        listNumber = 3

    return location, listNumber
