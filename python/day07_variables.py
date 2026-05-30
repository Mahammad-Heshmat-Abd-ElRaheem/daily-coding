############################## Variable names ##############################
# Variable names can only contain letters, numbers, and underscores (_).
# Variable names cannot start with a number.
# Variable names cannot be the same as Python keywords (reserved words).
# Variable names should be descriptive and meaningful.

# Examples of valid variable names:
from ast import Import


my_variable = 10
their_variable = 20
our_variable = 30

# Examples of invalid variable names:
# 1variable = 10  # Invalid: starts with a number
# variable-1 = 10  # Invalid: contains a hyphen
# variable 1 = 10  # Invalid: contains a space

############################## Reserved words ##############################
# Python has a set of reserved words that cannot be used as variable names.
# These include: 
# and, as, assert, break, class, continue, def, 
# del, elif, else, except, exec, finally, lambda,
# for, from, global, if, import, in, is, not, or, 
# pass, print, raise, return, try, while, with, yield

# Note: Python is case-sensitive, you can modify any of these words by changing the case of any letter, for example:
And = 10  # Valid: 'And' is not a reserved word, but 'and' is a reserved word
Import = 20  # Valid: 'Import' is not a reserved word, but 'import' is a reserved word


###################################### How to use a variable ##############################################
# To use a variable, simply type its name and assign it a value using the equals sign (=).
# Variables can be used to store different types of data, such as numbers, strings, lists, etc.
# Example of using variables:
age = 25  # Assigning an integer value to variable age
name = "Alice"  # Assigning a string value to variable name
account_balance = 1000.50  # Assigning a float value to variable account_balance
print("Name:", name,"\nAge:", age, "\nAccount Balance:", account_balance)  # Printing the values of the variables

# You can also perform operations using variables:
new_balance = account_balance + 500  # Adding 500 to the account balance

#You can use the print() function and combine text and variables using the + operator to output strings and variables. For example:
new_balance = "2500.50"  # Converting the new balance to a string for concatenation
print("New Account Balance: " + new_balance)  # Printing the new account balance
