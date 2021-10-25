# DataMan - CTS-285
# Lord Jenar Adolph C Allan
# 06/10/2021

"""
Disclaimer: Thank you Taylor J. Brown for your permission to
copy the basic calculator and calculation core.
______Sprint 1______ 
-New Content-
   
Main Menu:
-----------
    Placeholder functions and a menu displayed with working paths.
    
Basic Calculator:
------------------
    The caclulator use the operands in a menu and enter your number and passes 
    the equation through an if-elif-else code then displays the answer to 
    the entered equation using the choosen operand from the menu.
______Sprint 2______
Basic Calculator
-----------------
   Refactored, the processing component to a new module calculation core. 
   It now sends the string to the function and recives a tuple 
   to unpack and display.
Answer Checker
----------------
    The previous answer checker uses inputed equation from the previous basic
    calculator and see if you know your answer.
-New Content-
2 more options will be completed soon
"""

def main():
    print("\n","_"*7,"MENU","_"*7,"\n1. Normal Calculator\n2. Answer Checker\
              \n3. Memory Bank\n4. Number Guesser\n5. Exit", sep='')
    
    selector = int(input("Enter your selection\n >"))
    if selector == 1:
        normalCalculator()
          
    elif selector == 2:
        answerChecker()
    
    elif selector == 3:
        memoryBank()
    
    elif selector == 4:
        numberGuesser()
    
    elif selector == 5:
        print("\n Bye \n")
        pass
    else:
        print("Invalid input")
        


def normalCalculator():
    loop = True
    while loop == True:
        equate = input("Enter an equation or enter exit: ")
        val_print = calculator_core(equate)
        if len(val_print) > 0:
            x,y,z = val_print[0],val_print[1],val_print[2]
            operator = val_print[3]
            print(x, operator, y, "=", z)
        elif equate == 'exit':
            break
        else:
            print("invalid input")
def answerChecker():
    equation_list = []
    answer_list = []
    keep_going = True
    index = 0
    count = 0
    correct = 0
    incorrect = 0
    list_length = 1
    
    while keep_going == True:
        print("\nAnswer Checker")
        print("1. User made questions\n2. Ten random questions\n3. Exit")
        usr_inp = input("Enter choice here: ")
        
        if usr_inp == "1":
            print("Please enter 3 equations with the format in the\
                  \nparenthesis: (1+2)")
            for a in range(3):
                x = input(">")
                equation_list.append(x)
                answer = calculator_core(x)
                answer_list.append(answer[2])
        
            while len(answer_list) > 0:
                print(equation_list[index],"= ?")
                i = int(input("Answer :"))
                if i == answer_list[0]:
                    print("That is correct!")
                    correct += 1
                    index += 1
                    del answer_list[0]
                    if index == 3:
                        break
                elif count == 2:
                    print("Sorry but the answer was:", answer_list[0],"\n")
                    incorrect += 1
                    count = 0
                    index += 1
                    del answer_list[0]
                elif i != answer_list[0]:
                    print("Sorry that was incorrect")
                    count += 1
                    
            print("\nYou got", correct, "correct and", incorrect, "incorrect out of 10")
        elif usr_inp == "2":
            pass
        elif usr_inp == "3":
            keep_going = False
        else:
            print("Please choose a valid option!")

    
def memoryBank():
    print("Memory Bank")

def numberGuesser():
    print("Number Guesser")


    

        
        
def calculator_core(equate):
    """
     - Determines the type of equation entered by the operand seperating
         the two numbers entered.
     - Delete the operator from the string.
     - Split the equation into a list.
     - Preform appropriate process to equation and then return the results 
         in a tuple.
    """
    split_equate = []
    return_L = []
    
# Addition
    if "+" in equate:
      split_equate = equate.split("+")
      x = int(split_equate[0])
      y = int(split_equate[1])
      z = x + y
      return_L.extend((x,y,z))
      return_L.append("+")
      return return_L
      
# Subtraction
    elif "-" in equate:
      split_equate = equate.split("-")
      x = int(split_equate[0])
      y = int(split_equate[1])
      z = x - y
      return_L.extend((x,y,z))
      return_L.append("-")
      return return_L
        
# Division  
    elif "/" in equate:
      split_equate = equate.split("/")
      x = int(split_equate[0])
      y = int(split_equate[1])
      try:
          z = x / y
          return_L.extend((x,y,z))
          return_L.append("/")
          return return_L
      except ZeroDivisionError:
          print("You cannot divide by zero!")
      return
    
# Multiplication
    elif "*" in equate:
      split_equate = equate.split("*")
      x = int(split_equate[0])
      y = int(split_equate[1])
      z = x * y
      return_L.extend((x,y,z))
      return_L.append("*")
      return return_L
      
    elif equate == "exit" or "quit":
       return return_L
    else:
        print("That is not a valid equation.")

if __name__ == "__main__":
    main()
