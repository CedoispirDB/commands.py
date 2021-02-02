from math import sqrt


def getNext(line):
    position = line.index("")
    newLine = ""
    for i in range(0, len(line)):
        if i != position:
            # print(line[i])
            newLine = newLine + line[i]
        else:
            newLine = newLine + "|"
    # print(newLine)
    return newLine.index("/")


file = open("/Users/marcobarreirinhas/Programs/Python/math.txt", "r")

for line in file:
    print(line)
    if line.__contains__("sqrt"):
        result = sqrt(int(line[line.index("(") + 1: line.index(")")]))
    if line.__contains__("+"):
        print(int(result))