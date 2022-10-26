
code = ""
size = 44
i = 0

while len(code) <= 44:
    char = chr(i)
    print(char)
    if char != "":
        code = code + char
    i += 1


print(code)
