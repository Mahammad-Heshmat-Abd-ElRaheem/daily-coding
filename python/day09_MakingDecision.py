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

