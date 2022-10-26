import rightTriangle
from decimal import Decimal, getcontext

def digitPi(k):
    first = Decimal(4.0) / Decimal(8.0 * k + 1)
    second = Decimal(2.0) / Decimal(8.0 * k + 4)
    third = Decimal(1.0) / Decimal(8.0 * k + 5)
    forth = Decimal(1.0) / Decimal(8.0 * k + 6)
    sub = Decimal(first - second - third - forth)
    math = Decimal(1.0 / (16 ** k)) * sub

    return math



def summation(k):
    sum = Decimal(0)
    for i in range(k + 1):
        # print(f"for {i}: {digitPi(i)}")
        sum += digitPi(i)
    strSum = str(sum)
    print(sum)
    # print(f"{k} digit of PI: {strSum[k:k + 1]}")


summation(20)
# print("3.1415926535897932385")
print(str(Decimal(rightTriangle.pi)))


