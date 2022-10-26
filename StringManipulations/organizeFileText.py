file = open("/Users/marcobarreirinhas1/Programs/Python/UtilsTexts/numbers.txt", "r")
numbers = []

for lines in file:
    lines = lines.split()
    for n in lines:
        numbers.append(n)

file.close()
file = open("/Users/marcobarreirinhas1/Programs/Python/UtilsTexts/numbers.txt", "w")

for n in numbers:
    n = n.split(",")[0]
    file.write(n)
    file.write("\n")


