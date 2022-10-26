file = open("/Users/marcobarreirinhas1/Programs/Python/history.txt", "r")
newfile = []
for line in file:
    # print(line)
    line = line.split("\n")[0]

    if not line == "\n" and not line == " ":
        newfile.append(line + ":\n")

file.close()
file = open("/Users/marcobarreirinhas1/Programs/Python/history.txt", "w")
for line in newfile:
    print(line)
    file.write(line)