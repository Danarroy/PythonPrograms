width = int(input("Width: ")) # Get the width from the user
height = int(input("Height: ")) # Get the height from the user

for i in range(height): # Loop for the number of rows (height), if 3 , it will run 3 times onece for each row
    print("#" * width) # Print a row of hashes with the specified width
