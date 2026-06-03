#Using multiple arguments
print("The itsy bitsy spider" , "climbed up" , "the waterspout.")  # the output will be separated by spaces by default
# output: The itsy bitsy spider climbed up the waterspout.

# Positional arguments
print("My name is", "Python.")
print("Monty Python.")
# The output of the above code will be:
# My name is Python. 
# Monty Python.

#Keyword arguments
print("Monty Python.", end=" ") # end parameter changes the default newline to a space
print("I love programming in Python.")

# usully print() function separates its outputted arguments with spaces. This behavior can be changed
print("The itsy bitsy spider" , "climbed up" , "the waterspout.", sep="-") # sep parameter changes the default space separator to a hyphen


#Both keyword arguments may be mixed in one invocation, just like here in the editor window.
print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")