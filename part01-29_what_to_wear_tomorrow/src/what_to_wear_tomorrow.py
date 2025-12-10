"""
print("What is the weather forecast for tomorrow?")

temperature = int(input("Temperature: "))
rain = input("Will it rain? (yes/no):")

if temperature > 20 and rain == "no":
    print("Wear jeans and a T-shirt.")
elif temperature > 10 and rain == "no":
    print("Wear a jeans and a T-shirt.")
    print("I recommend taking a jumper as well")
elif temperature > 5 and rain == "no":
    print("Wear jeans and a T-shirt")
    print("I recommend taking a jumper as well")
    print("Take a jacket with you")
elif (temperature >= 0 and temperature <= 5) and rain == "yes":
    print("Wear jeans and a T-shirt")
    print("I recommend taking a jumper as well")
    print("Take a jacket with you")
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
    print("Don't forget your umbrella")
""" #my way

print("What is the weather forecast for tomorrow?")

temperature = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ").strip().lower()

print("Wear jeans and a T-shirt")

if temperature <= 20:
    print("I recommend a jumper as well")
if temperature <= 10:
    print("Take a jacket with you")
if temperature <= 5:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
if rain == "yes":
    print("Don't forget your umbrella!")
