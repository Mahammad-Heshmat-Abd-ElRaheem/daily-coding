# Python can generate random numbers using the built-in `random` module. Here's how you can generate a random number between 1 and 100:

# Generate a random number between 1 and 100
from random import random


random_number = random.randint(1, 100)
print("Random number:", random_number)

# You can also generate a random floating-point number between 0 and 1 using the `random()` function:
random_float = random.random()
print("Random float between 0 and 1:", random_float)

# If you want to generate a random number within a specific range, you can use the `randint()` function:
random_number_in_range = random.randint(10, 50)
print("Random number in range 10-50:", random_number_in_range)