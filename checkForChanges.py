print("MMM")

file1 = open("/Users/weKnow/t.txt", "r")
content1 =[]

file2 = open("/Users/weKnow/t2.txt", "r")
content2 = []

for lines1 in file1.readlines():
    content1.append(lines1.strip("\n"))

for lines2 in file2.readlines():
    content2.append(lines2.strip("\n"))

if len(content1) > len(content2):
    print("File one has more characters" + " with " + str(len(content1)) + " and file two has " + str(len(content2)))
    exit()
elif len(content1) < len(content2):
    print("File two has more characters" + " with " + str(len(content2)) + " and file one has " + str(len(content1)))
    exit()    

x = 0
for x in range(0, len(content1)):
    first = content1[x]
    second = content2[x]
    if first != second:
        print("Difference between: " + content1[x] + " and" + content2[x])
    x += 1


