while True:
    x = int(input("x: "))
    y = int(input("y: "))
    z = int(input("z: "))

    if z < y or z < x:
        print("WRONG INPUT")

    rightTriangle = x * x + y * y

    if rightTriangle == (z * z):
        print("is right triangle")
    else:
        print("it is not")
