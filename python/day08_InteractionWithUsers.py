#################################### How to interact with users in Python ####################################
# the answer is: The input() function
# The input() function allows you to take input from the user. It prompts the user to enter some data and returns it as a string.
# Example of using the input() function:
print("What is your name?")
name = input()  # This will wait for the user to enter their name and store it in the variable 'name'
print("Hello", name)  # This will greet the user by their name

############################# Using input() with a prompt ############################
# You can also provide a prompt directly within the input() function to make it more concise:
name = input("What is your name? ")  # This will display the prompt and wait for the user's input
print("Hello", name)
# The input() function always returns a string, so if you want to get a number from the user, you need to convert it using int() or float():

############################## Type casting (type conversions) ##############################
# Python offers two simple functions to specify a type of data and solve this problem - int() and float()
age = input("How old are you? ")  # This will return a string
age = int(age)  # Convert the string to an integer
print("You are", age, "years old.")
# You can also combine the input() function with type casting in one line:
age = int(input("How old are you? "))  # This will prompt the user and convert the input to an integer in one step
print("You are", age, "years old.")

############################## String operators ##############################
# You can use the + operator to concatenate strings, which means combining them together. For example:
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
full_name = first_name + " " + last_name
print("Your full name is:", full_name)

# You can also use the * operator to repeat a string multiple times. For example:
word = input("Enter a word: ")
print(word * 3)  # This will print the word three times in a row, without spaces in between. If you want to add spaces, you can do it like this:
print((word + " ") * 3)  # This will print the word three times with a space in between each repetition.   
