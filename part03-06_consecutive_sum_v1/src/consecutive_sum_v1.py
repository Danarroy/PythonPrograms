limit = int(input("Limit: "))

total = 0
next_number=1

while total < limit:
    total = total + next_number
    next_number = next_number + 1
print(total)
