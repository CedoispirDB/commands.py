def format(file, open, close):
    string = ""
    count = 0
    words = []
    for line in file:
        words.append(line.split("\n")[0])

    for line in words:
        if count % 8 == 0:
            skip = "\n"
        else:
            skip = ""
        if count == 0:
            string = open + '"' + line + '", '
        elif count == len(words) - 1:
            string = string + '"' + line + '"' + close
        else:
            string = string + '"' + line + '", ' + skip

        count += 1
    print(string)


# For an array
def formatArray(file, open, close):
    string = ""
    count = 0
    words = []
    for line in file:
        words.append(line.split("\n")[0])
    for line in words:
        for word in line:

            if count == 0:
                string = open + '"' + word + '", '
            elif count == 25:
                string = string + '"' + word + '"' + close
            else:
                string = string + '"' + word + '", '

            count += 1

    print(string)


format(open("/Users/marcobarreirinhas1/Programs/Python/UtilsTexts/words.txt", "r"), "[", "]")
s = ""
for line in open("/Users/marcobarreirinhas1/Programs/Python/UtilsTexts/words.txt", "r"):
    line = line.split("\n")
    for w in line:
        s = s + w

print(s)