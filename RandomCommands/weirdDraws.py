import time
from re import U
# "█"
# u"\u2581"
def printProgressBar(iteration, length, fill="█", printEnd="\n"):
    filledLength = iteration
    bar = fill * filledLength + ' ' * (length - filledLength)
    bar2 = ' ' * (length - filledLength) + fill * filledLength
    print(f'|{bar2}{bar}|', end=printEnd)
    if iteration == length:
        # print()
        pass


length = 40
bar = ""

for i in range(0, 102):
    bar = bar + "-"

print(bar)

for i in range(0, length):
    time.sleep(0.1)
    printProgressBar(i + 1, 50)

for i in range(0, 20):
    print("")
    pass
for i in range(0, length):
    time.sleep(0.1)
    printProgressBar(40 - i, 50)

print(bar)
