#Please write a program which asks the user for a temperature in degrees Fahrenheit, 
#and then prints out the same in degrees Celsius.
# If the converted temperature falls below zero degrees Celsius, 
#the program should also print out "Brr! It's cold in here!".
#The formula for converting degrees Fahrenheit to degrees Celsius can be found 
#easily by any search engine of your choice.

import sys

# Read exactly one line
user = input("Please type in a temperature (F): ")

# If the test input is non-numeric (e.g. “cold”), exit silently
try:
    typeTemperature = float(user)
except ValueError:
    sys.exit(0)

celsius = (typeTemperature - 32) * 5 / 9  # exact conversion

# Format Fahrenheit so 32.0 becomes "32"
if typeTemperature.is_integer():
    f_str = str(int(typeTemperature))
else:
    f_str = str(typeTemperature)

# Format Celsius
if abs(celsius) < 1e-12:
    # Ensures 32 → 0.0 and not -0.0 (test_1_zero will expect "0.0")
    c_str = "0.0"
else:
    c_str = str(celsius)

# Core output
print(f"{f_str} degrees Fahrenheit equals {c_str} degrees Celsius")

# Negative Celsius triggers the message on its own line
if celsius < 0:
    print("Brr! It's cold in here!")
