def formMultiplyString():
    listOfWords = open("/Users/marcobarreirinhas/Programs/Python/words.txt", "r")
    w = []
    for words in listOfWords:
        words = words.strip("\n")
        w.append(words)
    return w


def formatWords(words):
    listOfWords = words
    answer = ""
    for n in range(0, len(listOfWords)):
        answer = answer + '"' + listOfWords[n] + '" ,'

    print(answer)
formatWords(formMultiplyString())
