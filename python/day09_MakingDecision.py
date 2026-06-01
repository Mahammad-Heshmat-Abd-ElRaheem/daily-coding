# To ask questions, Python uses a set of very special operators. Let's go through them one after another

################################### Comparison: equality operator ###################################
#  the equality operator is ==, and it returns True if the two operands are equal, and False otherwise
print(1 == 1) # True
print(1 == 2) # False
print("hello" == "hello") # True
print("hello" == "Hello") # False


################################### Comparison: inequality operator ###################################
#  the inequality operator is !=, and it returns True if the two operands are not equal, and False otherwise
print(1 != 1) # False
print(1 != 2) # True
print("hello" != "hello") # False
print("hello" != "Hello") # True

################################### Comparison: greater than operator ###################################
#  the greater than operator is >, and it returns True if the left operand is greater than the right operand, and False otherwise
print(1 > 2) # False
print(2 > 1) # True
print(1 > 1) # False
print("b" > "a") # True because in the ASCII table, the value of "b" is greater than the value of "a"
print("a" > "b") # False

# if you can verify the Unicode values using ord() function
print(ord("a")) # 97
print(ord("b")) # 98

################################### Comparison: less than operator ###################################
#  the less than operator is <, and it returns True if the left operand is less than the right operand, and False otherwise
print(1 < 2) # True
print(2 < 1) # False
print(1 < 1) # False
print("a" < "b") # True
print("b" < "a") # False

################################### Comparison: greater than or equal to operator ###################################
#  the greater than or equal to operator is >=, and it returns True if the left operand is greater than or equal to the right operand, and False otherwise
print(1 >= 2) # False
print(2 >= 1) # True
print(1 >= 1) # True

################################### Comparison: less than or equal to operator ###################################
#  the less than or equal to operator is <=, and it returns True if the left operand is less than or equal to the right operand, and False otherwise
print(1 <= 2) # True   
print(2 <= 1) # False
print(1 <= 1) # True

################################### Making use of comparison operators ###################################
#  we can use comparison operators to make decisions in our code. For example, we can memorize the result of a comparison in a variable, and then use that variable to make a decision

number_of_students = 35
answer = number_of_students > 30
print(answer) # True

################################### Priority of comparison operators ###################################
#  comparison operators have a specific priority order:
# 1 - parentheses ()
# 2 - unary operators +, -
# 3 - the power operator **
# 4 - multiplication *, division /, floor division //, modulus %
# 5 - addition +, subtraction -
# 6 - comparison operators >, <, >=, <=
# 7 - equality operators ==, !=

# The operators == and != have lower priority than the comparison operators >, <, >=, <=
#  this means that in an expression like 1 == 2 > 3, the > operator is evaluated first, and then the == operator
print(1 == 2 > 3) # False
print(1 == 2 < 3) # False because 2 < 3 is True, but 1 == True is False
print(1 == 1 > 0) # True because 1 > 0 is True, and 1 == True is True