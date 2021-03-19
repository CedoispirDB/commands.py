from imgToBytes import turn_to_bytes, transform

proceed = True
option = ""

while proceed:
    option = input("Function: ")
    option = option.lower()
    if option != "b" and option != "i":
        print("\n" + "Please choose a valid function:" + "\n" +
              "Turn to bytes: b" + "\n" + "Get image: i" + "\n")
        proceed = True
    else:
        proceed = False

path = input("Path: ")
if path == "":
    path = "/Users/weKnow"

if option == "b":
    turn_to_bytes(path)
else:
    transform(path)

# /Users/heKnows
