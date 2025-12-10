print("Please type in integer numbers. Type in 0 to finish.")

numbers_list = [] # Initialize an empty list to store the numbers

while True: # Infinite loop to collect numbers
    n = int(input("Number: ")) # Read an integer from user input
    if n == 0: # If the input is 0, exit the loop
        break # Exit the loop
    numbers_list.append(n) #if n is not 0, add it to the list

print("... the program asks for numbers") # Indicate that the program is processing the numbers
print("Numbers typed in", len(numbers_list)) # Print the count of numbers entered the method len() counts the elements in the list
print("The sum of the numbers is", sum(numbers_list)) # Print the sum of the numbers using the sum() function
print("The mean of the numbers is", sum(numbers_list) / len(numbers_list)) # Calculate and print the mean of the numbers len gives the count of numbers so sum/lenght is the mean

positive_count = len([x for x in numbers_list if x > 0]) # Count how many numbers are positive, using a list comprehension
negative_count = len([x for x in numbers_list if x < 0]) # Count how many numbers are negative, using a list comprehension

print("Positive numbers", positive_count)
print("Negative numbers", negative_count)
