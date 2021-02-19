# Function to find permutations of a word (I forgot why I need I)
permutations = []


def findPermutations(word, ans):
    word = str(word.lower())

    if len(word) == 0:
        permutations.append(ans)
        return permutations

    for n in range(len(word)):
        digit = word[n]

        rest = word[0:n] + word[n + 1:]

        findPermutations(rest, ans + digit)

    return permutations


def divWord(words):
    newWords = []
    for n in range(len(words)):
        a = words[0:n + 1]
        b = words[n:]
        if len(a) >= 2:
            newWords.append(a)
        if len(b) >= 2:
            newWords.append(b)
    return newWords


def checkSimilarity(word, listA, accuracy):
    word = word.lower()
    listB = []
    letters = []
    answers = []
    count = 0
    leave = False

    percentage = accuracy / 100

    for n in listA:
        listB.append(n.lower())

    for n in word:
        letters.append(n)

    for n in listB:
        n = n.split()
        for k in n:
            for g in k:
                # print(g)
                if letters.__contains__(g) and (len(letters) + 2 >= len(k) >= len(letters) - 1):
                    # print("k len: " + str(len(k)))
                    count += 1

                accuracy = int(len(n) * percentage) + 1
                # print(accuracy)
                if count >= accuracy:
                    answers.append(n[0])
                    leave = True
                    break
            if leave:
                break
        count = 0

    # print(answers)

    answers2 = []
    for n in answers:
        if n.startswith(word[0]):
            answers2.append(n)

    # print(answers2)
    answers3 = []
    for n in answers2:
        for k in divWord(word):
            if n.__contains__(k):
                answers3.append(n)
                break

    if len(answers3) == 0 and len(answers2) != 0:
        return answers2
    elif len(answers3) != 0:
        return answers3
    else:
        return answers


# names = ["Akame", "Marcelo", "Agda", "Bia", "Julia", "Natalia", "Daniela", "Robinson", "Bianca", "Luana"]
# print(checkSimilarity("aame", names, 50))

# print(findPermutations("aame", ""))
# divWord("aame")
