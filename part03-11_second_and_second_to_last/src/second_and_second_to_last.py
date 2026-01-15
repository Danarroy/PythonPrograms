string = input("Please type in a string: ")


index_one = string[1]
index_two = string[len(string)-2]

if index_one == index_two:
    print("The second and the second to last characters are " + index_one)
else:
    print("The second and the second to last characters are different")