import math as math
import functions2 as func


def main():
    
    again="y"
    while again.lower()=="y":
        mainmenu()
        again=input("Would you like to calculate something else? (y/n): ")
        
        



    



def mainmenu():
    print("[1] Elliptic Torus Area")
    print("[2] Square Area")


def numberchoice():
    
    numberchoice= input("How would you like to calculate: ")
    if numberchoice == "1":
        func.torus()
    elif numberchoice == "2":
        func.square()
    else:
        input("Goodbye")

        


if __name__=="__main__":
    mainmenu()
    numberchoice()
