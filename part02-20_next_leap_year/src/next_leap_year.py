year = int(input("Year: ")) # get the year from the user
next_year = year + 1 # start checking from the next year 


while True: # while true
    if (next_year % 4 == 0 and next_year % 100 != 0) or (next_year % 400 == 0): #if leap year can be divided by 4 but not 100 or can be divided by 400
        print("The next leap year after", year, "is", next_year) # then print the next leap year
        break # exit the loop
    next_year += 1 # if not a leap year, check the next year


# 2028 %  4  is 0 because 2028 / 4 = 507 with no remainder
# 2028 % 100 is 28 because 2028 / 100 = 20 with a remainder of 28
# 2028 % 400 is 28 because 2028 / 400 = 5 with a remainder of 28 
# Example: 2028 is a leap year because it can be divided by 4 but not by 100