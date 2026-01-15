string = input("Please type in a string: ") # Get the string from the user

stars = 20 - len(string) # Calculate the number of stars needed for right alignment, 20 starts minus the length of the string, if string is dan it will be 20 - 3 = 17. stars = 17
print("*" * stars + string) # multiply * with stars which is 17, so * 17 + Dan
 #output *****************Dan