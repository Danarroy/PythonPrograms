string = input("Please type in a string: ") # string is methodology
substring = input("Please type in a substring: ") # substring is o

count = 0
i = 0

while i <= len(string) - len(substring): # while i <= 11 - 1 which is 10, i is 0. So its
    if string[i:i+len(substring)] == substring:
        count += 1
        if count == 2:
            print("The second occurrence of the substring is at index " + str(i) + ".")
            break
        i += len(substring)
    else:
        i += 1

if count < 2:
    print("The substring does not occur twice in the string.")
