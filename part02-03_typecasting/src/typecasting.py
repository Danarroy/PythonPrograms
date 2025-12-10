float_number = float(input("Please type in a number: ")) # Get user input and convert to float
print("Integer part: " + str(int(float_number))) # Convert float to int and then to string for concatenation
print("Decimal part: " + str(float_number - int(float_number))) # Calculate decimal part and convert to string for concatenation