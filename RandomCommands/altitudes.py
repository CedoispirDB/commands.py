import math
while True:
    hyp = input("hyp: ")
    baseBig = input("baseBig: ")
    baseSmall = input("baseSmall: ")

    if hyp != "":
        hyp = int(hyp)
    if baseBig != "":
        baseBig = int(baseBig)
    if baseSmall != "":
        baseSmall = int(baseSmall)

    if hyp == "":
        hyp = math.sqrt((baseBig * baseSmall))
        print("hyp: " + str(hyp))
    elif baseBig == "":
        baseBig = (hyp * hyp) / baseSmall
        print("baseBig: " + str(baseBig))
    elif baseSmall == "":
        baseSmall = (hyp * hyp) / baseBig
        print("baseSmall: " + str(baseSmall))


