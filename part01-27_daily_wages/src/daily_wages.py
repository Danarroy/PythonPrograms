# Please write a program which asks for the hourly wage, hours worked, 
# and the day of the week. The program should then print out the daily wages, 
# which equal hourly wage multiplied by hours worked, except on Sundays when the hourly wage is doubled.

hourlyWage = float(input("Hourly wage: "))
hoursWorked = float(input("Hours worked: "))
dayOfWeek = input("Day of the week: ")



if dayOfWeek == "sunday" or dayOfWeek == "Sunday":
    dailyWage = (hoursWorked*2) * hourlyWage
    print(f"Daily wages: {dailyWage} euros ")
    
elif dayOfWeek == "monday" or dayOfWeek == "Monday" or \
     dayOfWeek == "tuesday" or dayOfWeek == "Tuesday" or \
     dayOfWeek == "wednesday" or dayOfWeek == "Wednesday" or \
     dayOfWeek == "thursday" or dayOfWeek == "Thursday" or \
     dayOfWeek == "friday" or dayOfWeek == "Friday":
     dailyWage = hoursWorked * hourlyWage
     print(f"Daily wages: {dailyWage} euros ")
    
    