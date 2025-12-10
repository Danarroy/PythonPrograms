# Get input from the user
letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")

# Create a list of the letters
letters = [letter1, letter2, letter3]

# Sort the letters alphabetically
letters.sort()

# The middle letter is now the second item in the sorted list
print("The letter in the middle is", letters[1])
