import math 

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
