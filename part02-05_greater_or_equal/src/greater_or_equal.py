firstnumber = int(input("Please type in the first number: "))
secondnumber = int(input("Please type in the second number: "))

if firstnumber > secondnumber:
    print("The greater number was:" + str(firstnumber))
elif secondnumber > firstnumber:
    print("The greater number was:" + str(secondnumber))
else:
    print("The numbers are equal!")