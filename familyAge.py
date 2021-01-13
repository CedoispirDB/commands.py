from datetime import date
import platform

numbersOfLines = 29
count = 0
day = date.today().day
month = date.today().month
year = date.today().year
system = platform.system()

if system == "Darwin":
    ages = open("/Users/marcobarreirinhas/Programs/Python/familyAges.txt", "w")
elif system == "Windows":
    print("You don't have a path defined for " + system)
else:
    print("You don't have a path defined for " + system)


def getNext(line):
    position = line.index("/")
    newLine = ""
    for i in range(0, len(line)):
        if i != position:
            # print(line[i])
            newLine = newLine + line[i]
        else:
            newLine = newLine + "|"
    # print(newLine)
    return newLine.index("/")


with open("/Users/marcobarreirinhas/Programs/Python/familyBirths.txt", "r") as file:
    for lines in file:
        if count < numbersOfLines:
            name = lines[0: lines.index(":") + 1]
            birthDay = lines[lines.index(":") + 1: lines.index("/")]
            birthMonth = lines[lines.index("/") + 1: getNext(lines)]
            birthYear = lines[len(lines) - 5: len(lines)]
            if count == 27:
                birthYear = lines[len(lines) - 6: len(lines)]

            if int(birthMonth) >= month:
                if int(birthDay) > day:
                    year -= 1

            # print(birthDay)
            # print(getNext(lines))
            # print(birthMonth)
            # print(name)
            # print(age)
            # print(len(lines))
            # print(lines)
            print(name + (str(year - int(birthYear)) + " years"))
            ages.write(name + (str(year - int(birthYear)) + " years\n"))
            count += 1

ages.close()
