limit = int(input("Limit: "))

sum = 0 # Initialize sum of consecutive numbers
number = 1 # Initialize the next consecutive number
text = ""   # Initialize text representation of the sum

while sum < limit: # Continue until the sum reaches or exceeds the limit
    sum = sum + number # Add the next consecutive number to the sum
    text = text + str(number) # Append the number to the text representation

    if sum < limit: # If the sum has not yet reached the limit, add a plus sign
        text = text + " + "    # Add plus sign for next number

    number = number + 1 # Move to the next consecutive number

print("The consecutive sum: " + text + " = " + str(sum))
