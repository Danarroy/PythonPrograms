while True:
    number = int(input("Please type in a number: "))

    if number <= 0:
        print("Thanks and bye!")
        break  # exit the loop if number is 0 or negative

    # calculate factorial manually
    result = 1
    for i in range(1, number + 1):
        result *= i

    print("The factorial of the number " + str(number) + " is " + str(result))
