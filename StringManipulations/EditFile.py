file = open("/Users/marcobarreirinhas1/Desktop/meeting_saved_chat.txt", "r")
file2 = open("/Users/marcobarreirinhas1/Desktop/edited.txt", "w")
for lines in file:
    if not (lines.__contains__("Beatriz") or lines.__contains__("NATALIA")):
        print(lines)
        lines = lines.split(":")
        lines = lines[len(lines) - 1]
        if lines[0] == " ":
            file2.write(lines[1:])
        else:
            file2.write(lines)
