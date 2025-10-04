# If-Else Statements in Python
# --------------------------------
# The if-else statement is used for decision making in Python.
# It allows you to execute certain code blocks based on conditions.
#
# Syntax:
# if condition:
#     # code to execute if condition is True
# else:
#     # code to execute if condition is False

# Example 1: Simple if-else
num = 10
if num > 5:
	print("Number is greater than 5")
else:
	print("Number is not greater than 5")

# Example 2: if-elif-else (multiple conditions)
marks = 75
if marks >= 90:
	print("Grade: A+")
elif marks >= 80:
	print("Grade: A")
elif marks >= 70:
	print("Grade: B")
else:
	print("Grade: C or below")

# Example 3: Nested if
age = 20
if age >= 18:
	if age < 65:
		print("You are an adult.")
	else:
		print("You are a senior citizen.")
else:
	print("You are a minor.")
