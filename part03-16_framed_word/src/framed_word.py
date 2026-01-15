word = input("Word: ") # word is dan
width = 30 # width is 30

# Top border
print("*" * width) # Print 30 stars

# Calculate spaces for centering
padding = (width - 2 - len(word)) // 2 # 30 - 2 - 3 = 25 // 2 = 12. So padding is 12
extra = (width - 2 - len(word)) % 2 # 30 - 2 - 3 = 25 % 2 = 1. So extra is 1. Extra is used to handle odd spacing

# Middle line
print("*" + " " * padding + word + " " * (padding + extra) + "*") # * + 12 spaces + dan + 13 spaces + *

# Bottom border
print("*" * width) # Print 30 stars
