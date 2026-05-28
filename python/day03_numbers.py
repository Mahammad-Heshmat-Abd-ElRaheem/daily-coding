# we can print numbers (integers and floats) directly without converting them to strings
print(1000) # prints the integer 1000
print(3.14) # prints the float 3.14

# we can print negative value as well
print(-500) # prints the negative integer -500
print(+500) # prints the positive integer +500

# if the number is long we can add _ to improve readability
print(1_000_000) # prints the integer 1000000
print(3.141_592_653_589_793) # prints the float 3.141592653589793

# we can also print numbers in different bases using prefixes
print(0b1010) # prints the binary number 10 (base 2)
print(0o17) # prints the octal number 15 (base 8)
print(0x1F) # prints the hexadecimal number 31 (base 16)

# you can omit zero when it is the only digit in front of or after the decimal point.
print(.5) # prints the float 0.5
print(5.) # prints the float 5.0

""" 
for very large or very small numbers, you can use scientific notation
the letter e (or E) is used to indicate the power of 10  
for example, the speed of light, expressed in meters per second. Written directly it would look like this: 300000000
"""
print(3e8) # prints the float 300000000.0 (3 times 10 to the power of 8)
print(1.6e-19) # prints the float 1.6e-19 (1.6 times 10 to the power of -19)