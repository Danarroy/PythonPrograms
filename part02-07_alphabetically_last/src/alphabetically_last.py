firstword = input("Please type in the 1st word: ")
secondword = input("Please type in the 2nd word: ")

if firstword > secondword:
    print(firstword + " is alphabetically last")
elif secondword > firstword:
    print(secondword + " is alphabetically last")
else:
    print("You gave the same word twice")