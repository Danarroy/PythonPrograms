string = input("Please type in a string: ") # Get the string from the user

for i in range(len(string)): # Loop through the length of the string
    print(string[:i+1]) #start from index 0 and add 1
    