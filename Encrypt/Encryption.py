import sys


def getChar(sequence):
    answer = []
    while sequence != "":
        pos = int(sequence[0])
        comp = sequence[1:  pos + 1]
        sequence = sequence[pos + 1:]
        # print(comp)
        # answer = answer + comp
        # print(answer)
        answer.append(comp)
    return answer


# Receives the password and option (0 encrypt, 1 decrypt) multiple keys
# def XOREncript(password, x):
#     keys = []
#     length = 0
#     if x == 0:
#         keys = randomWord(len(password))
#         length = len(password)
#     elif x == 1:
#         keys = password[int((len(password) / 2)):]
#         length = int(len(password) / 2)
#
#     answer = ""
#     for n in range(length):
#         xorKey = keys[n]
#
#         # print("password = " + password[:n] + " + " + chr(ord(password[n]) ^ ord(xorKey)) + " + " + password[n + 1:])
#         # print("chr: " + chr(ord(password[n]) ^ ord(xorKey)))
#         answer = answer + chr(ord(password[n]) ^ ord(xorKey))
#     if x == 0:
#         return answer + keys
#     elif x == 1:
#         return answer

def XOREncript(password):
    xorKey = "P"
    answer = ""
    length = len(password)
    for n in range(length):
        # print("password = " + password[:n] + " + " + chr(ord(password[n]) ^ ord(xorKey)) + " + " + password[n + 1:])
        # print("chr: " + chr(ord(password[n]) ^ ord(xorKey)))
        answer = answer + chr(ord(password[n]) ^ ord(xorKey))

    return answer


def toASCII(password):
    length = len(password)
    answer = ""

    for n in range(length):
        comp = str(ord(password[n]))
        answer = answer + str(len(comp)) + comp

    return answer


def fromASCII(password):
    numbers = getChar(password)
    answer = ""
    for n in range(len(numbers)):
        answer = answer + chr(int(numbers[n]))
    return answer


def encrypt(string):
    # print("Init: " + string)
    string = XOREncript(string)
    # print("After XOR 1: " + string)
    string = toASCII(string)
    # print("After ASCII 2: " + string)
    string = XOREncript(string)
    # print("After XOR 3: " + string)
    string = toASCII(string)
    # print("After ASCII 4: " + string)
    string = XOREncript(string)
    # print("After XOR 5: " + string)
    return string


def decrypt(string):
    # print("Init: " + string)
    string = XOREncript(string)
    # print("After XOR 1: " + string)
    string = fromASCII(string)
    # print("After ASCII 2: " + string)
    string = XOREncript(string)
    # print("After XOR 3: " + string)
    string = fromASCII(string)
    # print("After ASCII 4: " + string)
    string = XOREncript(string)
    # print("After XOR 5: " + string)
    return string


if __name__ == '__main__':
    myPass = "bihbiica``bihca`abiibihca`abigbihca``ca`ebihca`abifbihbiica`cbihca`abigbihca``ca`ebihca`eca`cbihca`eca" \
             "`dbihca`eca`e"

    password = ""

    if len(sys.argv) > 1:
        password = str(sys.argv[1])
    else:
        print("Error: No argument")
        exit(0)

    password = encrypt(password)

    if password == myPass:
        sys.exit("true")
    else:
        sys.exit("false")
