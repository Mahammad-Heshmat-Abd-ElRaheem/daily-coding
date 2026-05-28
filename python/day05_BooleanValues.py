# These two Boolean values have strict denotations in Python:
print(True)  # prints the Boolean value True
print(False)  # prints the Boolean value False
# you have to take these symbols as they are, including case-sensitivity.
# In Python, the following values are considered False:
# - None
# - False
# - 0
# - "" (empty string)
# - [] (empty list)
# - {} (empty dictionary)
# All other values are considered True. For example:
print(bool(0))  # prints False
print(bool(1))  # prints True
print(bool("Hello"))  # prints True
print(bool([]))  # prints False
print(bool([1, 2, 3]))  # prints True