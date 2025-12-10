person1 = print("Person 1:")
personOneName = input("Name: ")
personOneAge = int(input("Age: "))

person2 = print("Person 2:")
personTwoName = input("Name: ") 
personTwoAge = int(input("Age: "))

if personOneAge > personTwoAge:
    print("The elder is " + personOneName)
elif personTwoAge > personOneAge:
    print("The elder is " + personTwoName)
else :
    print(personOneName + " and " + personTwoName + " are the same age!")
