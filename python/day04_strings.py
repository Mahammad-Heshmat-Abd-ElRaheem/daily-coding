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

################################ String indexing and slicing ##############################
#  you can access individual characters in a string using indexing
print("Hello, World!"[0]) # the output will be: H
print("Hello, World!"[1:5]) # the output will be: ello  
print("Hello, World!"[-6:-1]) # the output will be: World

################################ String methods ######################################
#  strings have many built-in methods that can be used to manipulate them
print("hello, world!".upper()) # the output will be: HELLO, WORLD!
print("HELLO, WORLD!".lower()) # the output will be: hello, world!
print("   hello, world!   ".strip()) # the output will be: hello, world!
print("hello, world!".replace("o", "0")) # the output will be: hell0, w0rld!
print("hello, world!".split(", ")) # the output will be: ['hello', 'world!']
print("hello, world!".find("world")) # the output will be: 7
print("hello, world!".startswith("hello")) # the output will be: True
print("hello, world!".endswith("!")) # the output will be: True
print("hello, world!".count("o")) # the output will be: 2
print("hello, world!".isalpha()) # the output will be: False (because of the comma and space)
print("hello".isalpha()) # the output will be: True
print("123".isdigit()) # the output will be: True
print("hello, world!".title()) # the output will be: Hello, World!
print("hello, world!".capitalize()) # the output will be: Hello, world!
print("hello, world!".center(20, "*")) # the output will be: ***hello, world!*******
print("hello, world!".ljust(20, "*")) # the output will be: hello, world!********
print("hello, world!".rjust(20, "*")) # the output will be: *******hello, world!
print("hello, world!".zfill(20)) # the output will be: 0000000000hello, world!
print("hello, world!".lstrip()) # the output will be: hello, world! (removes leading whitespace)
print("hello, world!".rstrip()) # the output will be: hello, world! (removes trailing whitespace)
print("hello, world!".partition(", ")) # the output will be: ('hello', ', ', 'world!')
print("hello, world!".rpartition(", ")) # the output will be: ('hello', ', ', 'world!')
print("hello, world!".splitlines()) # the output will be: ['hello, world!'] (splits on newlines)
print("hello, world!\nThis is a new line.".splitlines()) # the output will be: ['hello, world!', 'This is a new line.']
print("hello, world!".swapcase()) # the output will be: HELLO, WORLD! (swaps case of each character)
print("hello, world!".isupper()) # the output will be: False
print("HELLO, WORLD!".isupper()) # the output will be: True
print("hello, world!".islower()) # the output will be: True
print("HELLO, WORLD!".islower()) # the output will be: False
print("hello, world!".isprintable()) # the output will be: True
print("hello, world!\n".isprintable()) # the output will be: False
print("hello, world!".isidentifier()) # the output will be: False (because of the comma and space)
print("hello_world".isidentifier()) # the output will be: True
print("hello, world!".isdecimal()) # the output will be: False
print("123".isdecimal()) # the output will be: True
print("hello, world!".isnumeric()) # the output will be: False
print("123".isnumeric()) # the output will be: True
print("hello, world!".isascii()) # the output will be: True
print("hello, world! 👋".isascii()) # the output will be: False
