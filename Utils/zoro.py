from Automation.essayWriter import randomWord
from StringManipulations.makeString import formatWords, formMultiplyString

size = 22

file1 = open("/Users/marcobarreirinhas1/Programs/Python/UtilsTexts/words.txt", "w")
file2 = open("/Users/marcobarreirinhas1/Programs/Python/UtilsTexts/words2.txt", "w")

r1 = randomWord(size)
# r2 = randomWord(size)
r2 = "amcfbokvngwelhsqtpiuyj"
for n in r1:
    file1.write(n)
    file1.write("\n")

for n in r2:
    file2.write(n)
    file2.write("\n")

file1.close()
file2.close()

print("Reference: " + r1)
print("Result: " + r2)

formatWords(formMultiplyString(open("/Users/marcobarreirinhas1/Programs/Python/UtilsTexts/words.txt", "r")),
            formMultiplyString(open("/Users/marcobarreirinhas1/Programs/Python/UtilsTexts/words2.txt", "r")))
