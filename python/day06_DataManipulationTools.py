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

# Remainder (modulo): the result is the remainder of the division of the first argument by the second argument.
print(14 % 4)  # the result is 2, because 14 divided by 4 is 3 with a remainder of 2
print(14 % 4.) # the result is 2.0
print(14. % 4) # the result is 2.0
print(14. % 4.)# the result is 2.0
"""
As you can see, the result is two. This is why:

14 // 4 gives 3 → this is the integer quotient;
3 * 4 gives 12 → as a result of quotient and divisor multiplication;
14 - 12 gives 2 → this is the remainder.
"""
# Addition: the result is the sum of the two arguments.
print(5 + 7)    # the result is 12 
print(-5 + 7.)   # the result is 2.0
print(5. + 7)   # the result is 12.0
print(5. + -7.)  # the result is -2.0

# Subtraction: the result is the difference of the two arguments.
print(10 - 4)   # the result is 6
print(-10 - 4.)  # the result is -14.0
print(10. - 4)  # the result is 6.0
print(-10. - 4.) # the result is -14.0


########################################################## Operators and their priorities ###############################################
# Most of Python's operators have left-sided binding, which means that the calculation of the expression is conducted from left to right.
# This simple example will show you how it works. Take a look:
print(9 % 6 % 2)  # the result is 1, not 0, because the calculation is conducted from left to right
# The calculation is conducted in the following way:
# 9 % 6 gives 3 → this is the result of the first modulo operation;
# 3 % 2 gives 1 → this is the result of the second modulo operation

# But with th e exponentiation operator (**) the calculation is conducted from right to left, which means that the calculation of the expression is conducted from right to left.
print(2 ** 3 ** 2)  # the result is 512, not 64, because the calculation is conducted from right to left
# The calculation is conducted in the following way:
# 3 ** 2 gives 9 → this is the result of the first exponentiation operation;
# 2 ** 9 gives 512 → this is the result of the second exponentiation operation

############################################## List of priorities of operators in Python ###############################################
# 1. Parentheses ( )
# 2. Exponentiation (**)
# 3. Unary plus and minus (+x, -x)
# 4. Multiplication, division, floor division, and modulo (*, /, //, %)
# 5. Addition and subtraction (+, -)
