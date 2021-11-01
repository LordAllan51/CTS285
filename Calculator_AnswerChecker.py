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
______Sprint 3______
Answer Checker:
------------------
Answer checker core has been refactored and created a core for memory bank 
and answer checker options.
It also accepts how many questions they would like to enter.
-New Content-
Memory Bank
----------------
A random question where the user will be prompted with a random question and 
they will have 3 chances to get it right before the answer is given.
At the end of the game the total asked questions and the number correct answered
questions is shown.

It also accepts how many questions they would like to be asked for this specific
game mode.
Only uses addition, subtraction, and multiplication. The reasoon for that 
is that divition problems have decimal places and arent easily verified 
by the program.
______Sprint 4______

"""

import random


def main():
    """ Basic menu to send the user to other functions. """
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
    """
    - Gathers equation information and sends it to the calculator_core function.
    - Gets decoded answer back and splits the list apart.
    - If the list length is not greater than 0 the function aborts.
    - Prints out the solved equation.
    """
    print("\nJust Calculator\n")
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
    """ 
    - Asks the user how many equations they would like to enter
    - Iterates through a for loop to take user equations and sends them to the calculator_core
      function and send them back
    - Returned equations are seperated and appended to lists(equation_list and answer_list)
    - Sends both new lists to memory_answer_core function and asks the user to asnwer the questions.
    """
    print("\nAnswer Checker\n")
    equation_list = []
    answer_list = []

    c = int(input("How many questions would you like to input?"))
    print("Format Example: Number1+Number2")
    for _ in range(c):
        x = input("Enter equation/s here > ")
        equation_list.append(x)
        answer = calculator_core(x)
        answer_list.append(answer[2])
    
    answer_core(equation_list,answer_list,c) 
    
def memoryBank():
    """
    - Asks the user how many questions they want to be asked 
    - The program will automatically generate the first and second number and choose between 
      multiplication, subtraction or addition.
    - Then the program sends the generated equations to the memory_answer_core function and 
      asks the user to asnwer the questions.
    """
    print("\nMemory Bank\n")
    int_range = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14']
    equation_list, answer_list, n, m, s = [],[],[],[],[]
    c = int(input("How many questions would you like to be asked?"))
    
    for count in range(c):
        r = random.randint(0, 14)
        a = int_range[r]
        n.append(a)
        
        operators = ['+','-','*']
        r = random.randint(0, 2)
        a = operators[r]
        s.append(a)
        
        r = random.randint(0, 14)
        a = int_range[r]
        m.append(a)
        
        i = ''.join([n[count],s[count],m[count]])
        answer = calculator_core(i)
        answer_list.append(answer[2])
        equation_list.append(i)
        
    answer_core(equation_list,answer_list,c)
def numberGuesser():
    """
    - Ask the user to guess a number between 1-100
    - If the user guesses the correct number congradulate them and send back to menu
    - If the user guesses a number lower than the secret number tell them and let them guess again
    - If the user guesses a number higher than the secret number tell them and let them guess again 
    """
    print("Number Guesser")
    
def answer_core(equation_list,answer_list,c):
    equation_list = equation_list
    answer_list = answer_list
    index = 0
    count = 0
    correct = 0
    incorrect = 0

    while len(answer_list) > 0:
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
                
    print("\nYou got", correct, "correct and", incorrect, "incorrect out of", c,
          " questions.")
    return



            
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
