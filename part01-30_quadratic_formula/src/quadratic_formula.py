# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

Value1 = int(input("Enter the value of a: "))
Value2 = int(input("Enter the value of b: "))
Value3 = int(input("Enter the value of c: "))

discriminant = (Value2 ** 2) - (4 * Value1 * Value3) #discriminant is b^2 - 4ac this is used to determine the nature of the roots
sqrt_discriminant = sqrt(discriminant) #this is the square root of the discriminant
root1 = (-Value2 + sqrt_discriminant) / (2 * Value1)
root2 = (-Value2 - sqrt_discriminant) / (2 * Value1)

print("The roots are", root1, "and", root2)




# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5