#  escape character, which you should remember is played by the backslash
print("I like \"Monty Python\"")

# Python can use an apostrophe instead of a quote
print('I like "Monty Python"')
#  but if you want to use an apostrophe, you have to escape it
print('I\'m Monty Python.') # or
print("I'm Monty Python.")

###################### Raw strings and multi-line strings ######################
#  you can also use a raw string, which ignores escape characters
print(r"I'm Monty Python.") 
#  triple quotes can also be used for multi-line strings
print("""This is a multi-line string.
It spans multiple lines.""")    
#  you can also use triple quotes for single-line strings
print("""This is a single-line string.""")

########################### String concatenation and repetition ###########################
#  you can concatenate strings using the + operator
print("Hello, " + "World!") #the output will be: Hello, World!
#  you can also repeat strings using the * operator
print("Hello, " * 3) # the output will be: Hello, Hello, Hello,
