# CSC 221
# M1H1 - Calculator
# Lord Jenar Adolph C Allan
# 8/16/2021

def Add():
    keepgoing = 0
    while keepgoing == 0:
        num1 = int(input("Enter a number:"))
        num2 = int(input("Enter a number:"))
        sums = num1 + num2
        print()
        print(num1,"+",num2,"=",sums)
        
        validation = 0
        keepgoing = rep(validation)
    
def Subtract():
    num1 = int(input("Enter a number:"))
    num2 = int(input("Enter a number:"))
    difference = num1 - num2
    print()
    print(num1,"-",num2,"=",difference)
    
def Divide():
    num1 = int(input("Enter a number:"))
    num2 = int(input("Enter a number:"))
    quotient = num1 // num2
    print()
    print(num1,"/",num2,"=",quotient)

def Multiply():
    num1 = int(input("Enter a number:"))
    num2 = int(input("Enter a number:"))
    product = num1 * num2
    print()
    print(num1,"*",num2,"=",product)

def rep(validation):
    while validation == 0:
        print("1. Repeat")
        print("2. Main Menu")
        select = int(input("Enter a number:"))
        print()
        if select == 1:
            return (0)
        elif select == 2:
            return (1)
        else:
            print("Invalid option! Please choose within 1 and 2.")
        
def DisplayMenu():
    print("Welcome to the calculator program")
    print("1. Add")
    print("2. Subtract")
    print("3. Divide")
    print("4. Multiply")
    print("5. Exit")
    print()

def mainMenu():
    ''' This menu function is formatted to prevent error '''
    loop = '1'
    while loop == '1':
        DisplayMenu()
        selection = input("Enter your choice: ")
        if selection == '1':
            print()
            Add()
            
        elif selection == '2':
            print()
            Subtract()
            
        elif selection == '3':
            print()
            Divide()
            
        elif selection == '4':
            print()
            Multiply()
            
        elif selection == '5':
            print()
            loop = '2'
            print()
            print("Bye!")
            ##raise SystemExit(0)#exit feature for spyder#REMOVED
        else:
            print()
            print("Invalid input/choice. Choose within 1-4")
        
if __name__ == "__main__":
    mainMenu()
