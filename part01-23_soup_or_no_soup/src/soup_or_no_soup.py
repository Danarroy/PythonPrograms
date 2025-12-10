name = input("Please tell me your name: ") # Ask for user's name

if name == "Jerry": # Check if user's name is "Jerry"
    print("Next please!") # If it is, print a message

    
else:  # If the name is not "Jerry", ask for soup portions
    portions = int(input("How many portions of soup? ")) # Ask for number of soup portions
    print(f"The total cost is {portions * 5.90}") # Calculate and print total cost
    print("Next please!") # End of the program