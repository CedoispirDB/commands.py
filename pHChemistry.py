import math

H = input("H(Just the exponent): ")
pH = input("pH: ")
OH = input("OH(Just the exponent): ")
pOH = input("pOH: ")

if pOH == "" and H == "" and pH == "":
    # I have just OH
    print("pOH: " + str(-math.log10(int(OH))))
    H = abs(14 - int(OH))
    print("H: " + str(H))
    print("pH: " + str(-math.log10(H)))
elif pOH == "" and OH == "" and pH == "":
    # I have just H
    print("pH: " + str(-math.log10(int(10 ** H))))
    pOH = -math.log10(int(H))
    pH = abs(14 - int(pOH))
    OH = 10 ** (-pOH)
    print("OH: " + str(OH))
    print("pOH: " + str(-math.log10(OH)))
elif H == "" and OH == "" and pH == "":
    # I have just pOH
    print("OH: " + str(10 ** -int(pOH)))
    H = abs(14 - int(OH))
    print("H: " + str(H))
    print("pH: " + str(-math.log10(H)))
elif H == "" and OH == "" and pOH == "":
    # I have just pH
    print("H: " + str(10 ** -int(pH)))
    OH = abs(14 - int(H))
    print("OH: " + str(OH))
    print("pOH: " + str(-math.log10(OH)))
elif pOH == "" and pH == "":
    # I have H and OH
    mySum = OH + H
    if mySum != 14:
        print("Either OH or H is wrong")
    print("pH: " + str(-math.log10(int(H))))
    print("pOH: " + str(-math.log10(int(OH))))
elif H == "" and OH == "":
    print("H: " + str(10 ** -int(pH)))
    print("OH: " + str(10 ** -int(pOH)))
    mySum = str(10 ** -int(pH)) + str(10 ** -int(pOH))
    if mySum != 14:
        print("Something is wrong")
elif OH == "":
    print("OH: " + str(10 ** -int(pOH)))
elif H == "":
    print("H: " + str(10 ** -int(pH)))
elif pOH == "":
    print("pOH: " + str(-math.log10(int(OH))))
elif pH == "":
    print("pH: " + str(-math.log10(int(H))))
