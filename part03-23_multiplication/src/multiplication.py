number = int(input("Please type in a number: ")) # Get the number from the user

for i in range(1, number + 1): #outer loop, then we print the multiplication table for each number from 1 to the number the user typed in, if number is 3 we will print the multiplication table for 1, 2 and 3
    for j in range(1, number + 1): #inner loop, we will print the multiplication table for each number from 1 to the number the user typed in, if number is 3 we will print the multiplication table for 1, 2 and 3
        print(f"{i} x {j} = {i * j}")
