from random import randint


def formMultiplyString(file):
    listOfWords = file
    w = []
    for words in listOfWords:
        words = words.strip("\n")
        w.append(words)
    return w


def formRandomList(x):
    randN = []
    count = 0
    while count <= x:
        r = randint(0, x)
        if not randN.__contains__(r):
            randN.append(r)
            count += 1
    return randN


def formatWords(words, words2):
    listOfWords = words
    listOfWords2 = words2
    answer = ""
    q = ""
    count = 0
    length = len(listOfWords) - 1
    r = formRandomList(length)
    n = 0
    while n <= length:
        count += 1
        k = listOfWords[r[n]]
        m = listOfWords2[r[n]]
        if (r[n] + 1) < length:
            q = listOfWords[r[n] + 1]

        if q == "":
            length -= 1

        if k != "":
            if length + 1 == count:
                answer = answer + '("' + k + '"' ", " '"' + m + '")'
            else:
                answer = answer + '("' + k + '"' ", " '"' + m + '"), '
        n += 1

    print(answer)


# listOfWords = []
# listOfWords.sort()
# The two lists must be the same size
# formatWords(formMultiplyString(open("/Users/marcobarreirinhas1/Programs/Python/words.txt", "r")),
#             formMultiplyString(open("/Users/marcobarreirinhas1/Programs/Python/words2.txt", "r")))
