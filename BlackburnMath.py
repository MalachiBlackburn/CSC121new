#Chetan Gongidi
#2/6/18
#CSC121
#This program displays several choices from a menu


def main():
    keepGoing = 'y'
    while keepGoing == 'y':
        menu()
        keepGoing = input("Do you want to keep going? Press y if yes: ")


def menu():
    choice = getChoice()
    if choice == 1:
        print ("Pizza")
    elif choice == 2:
        print("Burgers")
    elif choice == 3:
        print ("Tacos")
    elif choice == 4:
        print ("Chicken")
    else:
        print ("Enter only numbers 1-4")
        


def getChoice():
    
    getChoice = int(input("If you want Pizza type 1, if you want Burgers type 2, if you want Tacos type 3, if you want Chicken type 4: "))
    return getChoice



main()
