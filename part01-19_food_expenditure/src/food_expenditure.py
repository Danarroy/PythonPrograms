number1 = int(input("How many times a week do you eat at the student cafeteria?"))
number2 = float(input("The price of a typical student lunch?"))
number3 = float(input("How much money do you spend on groceries in a week?"))

print("Average food expenditure: ")
print(f"Daily: {(number1 * number2 + number3) / 7} euros")
print(f"Weekly: {(number1 * number2 + number3) / 1} euros")