num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# Swapping the values
temp = num1 
num1 = num2
num2 = temp
print("After swapping:")
print("First number:", num1)
print("Second number:", num2)

# Alternatively, you can swap two variables in Python without using a temporary variable:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Swapping the values without a temporary variable
num1, num2 = num2, num1
print("After swapping:")
print("First number:", num1)
print("Second number:", num2)