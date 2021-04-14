import time


def printProgressBar(iteration, length, i, fill="█", printEnd="\n"):
    filledLength = iteration
    space = " " * iteration
    fill2 = ' ' * (50 - i) + fill
    print(f'{space}{fill * i}', end=printEnd)
    if iteration == length:
        # print()
        pass


# length = 25
# x = 0
# i = 0
# while x <= length:
#     time.sleep(0.1)
#     printProgressBar(i * 2, 50, i)
#     x += 1
#     i += 1
#
fill = "█"
x = 4
bar = " " * 35 + fill * 40
bar2 = " " * 28 + fill * 7 + " " * 40 + fill * 7
bar3 = " " * 24 + fill * x + " " * 54 + fill * x
bar4 = " " * 20 + fill * x + " " * 61 + fill * x
bar5 = " " * 16 + fill * x + " " * 69 + fill * x
bar6 = " " * 13 + fill * x + " " * 76 + fill * x
bar7 = " " * 10 + fill * x + " " * 83 + fill * x
bar8 = " " * 6 + fill * x + " " * 91 + fill * x
bar9 = " " * 2 + fill * x + " " * 98 + fill * x

print(bar)

print(bar2)

print(bar3)

print(bar4)

print(bar5)
print(bar5)

print(bar6)
print(bar6)

for n in range(0, 5):
    print(bar7)

for n in range(0, 2):
    print(bar8)

for n in range(0, 2):
    print(bar8)

for n in range(0, 5):
    print(bar7)

print(bar6)
print(bar6)

print(bar5)
print(bar5)

print(bar4)

print(bar3)

print(bar2)

print(bar)
