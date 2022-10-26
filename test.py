def XOREncript(password):
    xorKey = "G"
    answer = ""
    length = len(password)
    for n in range(length):
        # print("password = " + password[:n] + " + " + chr(ord(password[n]) ^ ord(xorKey)) + " + " + password[n + 1:])
        # print("chr: " + chr(ord(password[n]) ^ ord(xorKey)))
        answer = answer + chr(ord(password[n]) ^ ord(xorKey))

    return answer

print("answer: ∫" + XOREncript("marco") + "∫")
