
node1 = open("/Users/marcobarreirinhas1/Desktop/Node1.txt", "r")
node2 = open("/Users/marcobarreirinhas1/Desktop/Node2.txt", "r")

arr1 = []
arr2 = []

for line in node1:
    arr1.append(line.split("\n")[0])

for line in node2:
    arr2.append(line.split("\n")[0])

ctn = 0
for i in range(len(arr1)):
    if arr1[i] == arr2[i]:
        ctn += 1
        print(arr1[i])

print(ctn)