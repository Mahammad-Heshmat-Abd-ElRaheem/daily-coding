# Python as a calculator
print(2 + 3)  # prints 5
print(10 - 4)  # prints 6
print(7 * 8)  # prints 56
print(15 / 3)  # prints 5.0

# Basic operators which are used for data manipulation:
# - Addition (+)
# - Subtraction (-)
# - Multiplication (*)
# - Division (/)
# - Modulo (%)
# - Exponentiation (**)
# - Floor Division (//)

# Exponentiation operator (**) is used to calculate the power of a number.
print(2 ** 3)   # the result is 8
print(2 ** 3.)  # the result is 8.0
print(2. ** 3)  # the result is 8.0
print(2. ** 3.) # the result is 8.0
# when both ** arguments are integers, the result is an integer, too;
# when at least one ** argument is a float, the result is a float, too.

# Multiplication operator (*) can also be used to repeat sequences:
print(2 * 3)    # the result is 6
print(2 * 3.)   # the result is 6.0
print(2. * 3)   # the result is 6.0
print(2. * 3.)  # the result is 6.0

# Division: the result is always a float, even if both arguments are integers.
print(10 / 2)   # the result is 5.0 
print(10 / 3)   # the result is 3.3333333333333335
print(10 / 3.)  # the result is 3.3333333333333335
print(10. / 3)  # the result is 3.3333333333333335
print(10. / 3.) # the result is 3.3333333333333335

# Integer division (floor division): the result is the largest integer less than or equal to the division result.
print(10 // 3)   # the result is 3
print(10 // 3.)  # the result is 3.0
print(10. // 3)  # the result is 3.0
print(10. // 3.) # the result is 3.0
# the results are always rounded; the result is an integer if both arguments are integers, and a float if at least one argument is a float.
# note: This is very important: rounding always goes to the lesser integer
print(-6 // 4)  # the result is -2, not -1, because -2 is less than -1
print(6. // -4) # the result is -2.0, not -1.0, because -2.0 is less than -1.0



