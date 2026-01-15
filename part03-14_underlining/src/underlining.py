while True: # Start an infinite loop because we don't know how many strings the user will input
    string = input("Please type in a string: ") # Prompt the user to input a string
    if string == "": # If the input string is empty, break the loop
        break # Exit the loop
    print(string) #if the string is not empty, print the string 
    print("-" * len(string)) # and then print a line of dashes with the same length as the string