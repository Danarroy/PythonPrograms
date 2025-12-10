#Please write a program which asks the user for two numbers and an operation. 
#If the operation is add, multiply or subtract, 
#the program should calculate and print out the result of the operation with the given numbers. 
#If the user types in anything else, the program should print out nothing.#


number1 = int(input("Number 1: ")) # Input from user
number2 = int(input("Number 2: ")) # Input from user 

operation = input("Operation: ") # Input for operation

add = (number1 + number2) # Add the two numbers
subtract = (number1 - number2) # Subtract the two numbers  
multiply = (number1 * number2) # Multiply the two numbers

if operation == "add": # Check if operation is add
    print(f"{number1} + {number2} = {add}")  #f does string formatting by replacing the variables in the string
elif operation == "subtract": # Check if operation is subtract
    print(f"{number1} - {number2} = {subtract}")
elif operation == "multiply": # Check if operation is multiply
    print(f"{number1} * {number2} = {multiply}")
