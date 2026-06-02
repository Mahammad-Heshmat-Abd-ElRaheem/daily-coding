########################################################################################
# If Condition
########################################################################################
# If condition is used to execute a block of code only if a specified condition is true.
# The syntax of an if statement is as follows:
# if condition:
#     block of code
# The condition is a boolean expression that evaluates to either True or False. If the condition is True, the block of code is executed. If the condition is False, the block of code is skipped.
# Example of an if statement
""" 
if the_weather_is_good:
    print("Let's go for a walk.")

if sheep_counter >= 50 :
    print("There are enough sheep to make a wool blanket.")
"""

age = 18
if age >= 18:
    print("You are eligible to vote.")

################################################################################ 
# If-else condition
################################################################################
# The if-else condition is used to execute one block of code if a specified condition is true, and another block of code if the condition is false.
# The syntax of an if-else statement is as follows: 
# if condition:
#     block of code to be executed if the condition is true
# else:
#     block of code to be executed if the condition is false

age = int(input("Please enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

################################################################################
# Nested if-else statements
################################################################################
# Nested if-else statements are if-else statements that are contained within another if-else statement. They are used to check multiple conditions in a hierarchical manner.
# The syntax of a nested if-else statement is as follows:   
# if condition1:
#     block of code to be executed if condition1 is true   
#     if condition2:
#         block of code to be executed if condition2 is true
#     else:
#         block of code to be executed if condition2 is false
# else:
#     if condition3:
#         block of code to be executed if condition3 is true
#     else:
#         block of code to be executed if condition3 is false

age = int(input("Please enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
    if age >= 21:
        print("You are also eligible to drive.")
    else:
        print("You are not eligible to drive.")