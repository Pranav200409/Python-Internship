'''Create a Python program that acts as a basic calculator.
It should prompt the user to enter two numbers and an operator (+ , - , * , / , %), and then display the result of the operation.'''

def add (x,y):
    return x+y

def sub(x,y):
    return x-y

def multi(x,y):
    return x*y

def divide(x,y):
    if y!=0:
        return x/y
    else:
        print("Division by 0 is not possible.")

def modulas(x,y):
    return x%y

print("\n\t\t Basic CALCULATOR using PYTHON")

while True:
    num1=float(input("\nEnter an number of your choice:"))
    num2 = float(input("Enter another number of your choice:"))
    operator = input("Choose any one operator (+, - , * , /, % ):")

    if (operator =='+'):
        result = add(num1,num2)
    elif (operator == '-'):
        result = sub(num1,num2)
    elif (operator =='*'):
        result = multi(num1,num2)
    elif (operator == '/'):
        result = divide(num1,num2)
    elif(operator =='%'):
        result = modulas(num1,num2)
    else :
        print("Error !!! :Invalid operator , please enter correct operator .")
        continue

    print(f"The result of {num1} {operator} {num2} is : {result}")

    continue_choice =input("\nDo you want to try again ? (yes to CONTINUE or no to EXIT):").strip().lower()
    if continue_choice != 'yes':
        print("Thank You !!!! EXITING")
        break
