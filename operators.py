
# 4. Membership Operators
# Used to test if a value is present in a sequence (like list, tuple, string, set, or dictionary)
nums = [1, 2, 3, 4, 5]
name = "Sharjeel"

# 'in': Returns True if value is found in the sequence
print(3 in nums)        # Output: True (3 is in the list nums)
print('a' in name)      # Output: True ('a' is in the string name)

# 'not in': Returns True if value is NOT found in the sequence
print(10 not in nums)   # Output: True (10 is not in the list nums)
print('z' not in name)  # Output: True ('z' is not in the string name)

# Operators in Python
# Operators are special symbols used to perform operations on variables and values.

# 1. Arithmetic Operators
# Used for mathematical calculations
a = 10
b = 3

# Addition
print(a + b)  # Output: 13 (Adds a and b)

# Subtraction
print(a - b)  # Output: 7 (Subtracts b from a)

# Multiplication
print(a * b)  # Output: 30 (Multiplies a and b)

# Division
print(a / b)  # Output: 3.333... (Divides a by b, returns float)

# Floor Division
print(a // b)  # Output: 3 (Divides a by b, returns integer part)

# Modulus
print(a % b)  # Output: 1 (Remainder of a divided by b)

# Exponentiation
print(a ** b)  # Output: 1000 (a raised to the power of b)


# 2. Logical Operators
# Used to combine conditional statements
x = True
y = False

# and: Returns True if both statements are true
print(x and y)  # Output: False

# or: Returns True if at least one statement is true
print(x or y)  # Output: True

# not: Reverses the result, returns False if the result is true
print(not x)  # Output: False


# 3. Comparison Operators (for reference)
# Used to compare two values, result is True or False
print(a == b)  # False (Equal to)
print(a != b)  # True (Not equal to)
print(a > b)   # True (Greater than)
print(a < b)   # False (Less than)
print(a >= b)  # True (Greater than or equal to)
print(a <= b)  # False (Less than or equal to)


# 4. Membership Operators
# Used to test if a value is present in a sequence (like list, tuple, string, set, or dictionary)
nums = [1, 2, 3, 4, 5]
name = "Sharjeel"

# 'in': Returns True if value is found in the sequence
print(3 in nums)        # Output: True (3 is in the list nums)
print('a' in name)      # Output: True ('a' is in the string name)

# 'not in': Returns True if value is NOT found in the sequence
print(10 not in nums)   # Output: True (10 is not in the list nums)
print('z' not in name)  # Output: True ('z' is not in the string name)



# 5. String Operators
# Strings support several operators for manipulation and comparison.
str1 = "Hello"
str2 = "World"

# Concatenation (+): Joins two strings
print(str1 + " " + str2)  # Output: Hello World

# Repetition (*): Repeats the string n times
print(str1 * 3)  # Output: HelloHelloHello

# Comparison (==, !=, >, <, >=, <=): Compares strings lexicographically
print(str1 == str2)  # Output: False
print(str1 != str2)  # Output: True
print("abc" < "bcd")  # Output: True (compares alphabetically)

# Membership (in, not in): Checks if substring exists in string
print("ell" in str1)  # Output: True
print("z" not in str2)  # Output: True

# Indexing: Access individual characters
print(str1[1])  # Output: e

# Slicing: Get substring
print(str2[1:4])  # Output: orl

