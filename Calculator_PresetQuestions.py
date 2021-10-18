class Question:
    """class for holding room names descriptions, exits"""
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def __str__(self):
        """Question Printer"""
        questText = "Question: "+ self.num1 + "\n" \
        + "Description: " + self.num2
        return questText + "\n"





# Function to add two numbers 
def add(num1, num2):
    return num1 + num2
  
# Function to subtract two numbers 
def subtract(num1, num2):
    return num1 - num2
  
# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2
  
# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2

"""Validation to check the answers"""
def validate(select,num1,num2,ans):
    if select == 1:
        user_ans=int(input("Your answer?\n"))
        if user_ans == ans:
            print("Congratulations!")
        else:
            print("Wrong Answer. Try Again!")
    elif select == 2:
        if select == 1:
            user_ans=int(input("Your answer?\n"))
        if user_ans == ans:
            print("Congratulations!")
        else:
            print("Come on! You can do it!")
      
    elif select == 3:
        if select == 1:
            user_ans=int(input("Your answer?\n"))
        if user_ans == ans:
            print("Congratulations!")
        else:
            print("Practice more!")
      
    elif select == 4:
        if select == 1:
            user_ans=int(input("Your answer?"))
        if user_ans == ans:
            print("Congratulations!")
        else:
            print("Try again please.")
    
    
def Parent():
    loop = True
    while loop == True:
        select = int(input("Select operations form 1, 2, 3, 4,(5 to quit) :"))
          
        number_1 = int(input("Enter first number: "))
        number_2 = int(input("Enter second number: "))
          
        if select == 1:
            print(number_1, "+", number_2, "=")
            ans = add(number_1, number_2)
            
          
        elif select == 2:
            print(number_1, "-", number_2, "=")
            ans = subtract(number_1, number_2)
            
          
        elif select == 3:
            print(number_1, "*", number_2, "=")
            ans = multiply(number_1, number_2)
            
          
        elif select == 4:
            print(number_1, "/", number_2, "=")
            ans = divide(number_1, number_2)
            
        elif select == 5:
            loop = False
            main()
        else:
            print("Invalid input")
        
    pass
    
    
def Student():
    loop = True
    while loop == True:
        print("Please select operation -\n" \
                "1. Add\n" \
                "2. Subtract\n" \
                "3. Multiply\n" \
                "4. Divide\n")
          
          
        # Take input from the user 
        select = int(input("Select operations form 1, 2, 3, 4,(5 to quit) :"))
          
        number_1 = int(input("Enter first number: "))
        number_2 = int(input("Enter second number: "))
          
        if select == 1:
            print(number_1, "+", number_2, "=")
            ans = add(number_1, number_2)
            validate(select,number_1,number_2,ans)
          
        elif select == 2:
            print(number_1, "-", number_2, "=")
            ans = subtract(number_1, number_2)
            validate(select,number_1,number_2,ans)
          
        elif select == 3:
            print(number_1, "*", number_2, "=")
            ans = multiply(number_1, number_2)
            validate(select,number_1,number_2,ans)
          
        elif select == 4:
            print(number_1, "/", number_2, "=")
            ans = divide(number_1, number_2)
            validate(select,number_1,number_2,ans)
        elif select == 5:
            loop = False
            main()
        else:
            print("Invalid input")

def main():
    print("Please select mode -\n" \
            "1. Parent\n" \
            "2. Student\n" \
            "3. Quit\n" \
                )
    
    selector = int(input("Enter your selection\n"))
    if selector == 1:
        Parent()
          
    elif selector == 2:
        Student()
        
    elif selector == 3:
        print("\n Bye \n")
        pass
    else:
        print("Invalid input")
        
if __name__ == "__main__":
    main()
