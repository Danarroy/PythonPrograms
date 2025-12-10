Userword = input("Please type in a word: ") # Get user input
number_of_letters = len(Userword) #create a variable to count the number of characters in the word #len function

if number_of_letters > 1:
    print("There are "+ str(number_of_letters) + " letters in the word " + Userword) #str function to convert number to string
print("Thank you!")
