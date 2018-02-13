def addition():
    first=int(input("Enter your first number: "))
    second=int(input("Enter your second number: "))
    add=first+second
    print(first, "+", second, "=", add)

def subtraction():
    first=int(input("Enter your first number: "))
    second=int(input("Enter your second number: "))
    sub=first-second
    print(first, "-", second, "=", sub)

def multiplication():
    first=int(input("Enter your first number: "))
    second=int(input("Enter your second number: "))
    mult=first*second
    print(first, "*", second, "=", mult)

def division():
    first=int(input("Enter your first number: "))
    second=int(input("Enter your second number: "))
    div=first/second
    print(first, "/", second, "=", div)

def integerdivision():
    first=int(input("Enter your first number: "))
    second=int(input("Enter your second number: "))
    intdiv=first//second
    print(first, "//", second, "=", intdiv)

def torus():
    majorradius=float(input("Enter your major radius: "))
    minorradius=float(input("Enter your minor radius: "))
    if majorradius <= minorradius:
        print("Major radius must be larger than the minor radius")
        torus()
    else:
        torusminor=(math.pi)*((minorradius)*(minorradius))
        torusmajor=(2*math.pi)*(majorradius)
        torusfinal= (torusminor)*(torusmajor)
        print("The volume of the torus is:", torusfinal)

def square():
    side=int(input("Enter the length of one side of the square: "))
    squarearea=side*side
    print("The area of the square is: ", squarearea)
