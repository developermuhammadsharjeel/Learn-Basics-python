# Match Statement in Python (Python 3.10+)
# ----------------------------------------
# The match statement is used for pattern matching, similar to switch-case in other languages.
# It allows you to compare a value against several patterns and execute code based on which pattern matches.
#
# Syntax:
# match variable:
#     case pattern1:
#         # code block
#     case pattern2:
#         # code block
#     case _:
#         # default block (like else)

# Example 1: Simple match-case
day = "Monday"
match day:
	case "Monday":
		print("Start of the work week!")
	case "Friday":
		print("End of the work week!")
	case _:
		print("Midweek day.")

# Example 2: Matching integers
num = 2
match num:
	case 1:
		print("One")
	case 2:
		print("Two")
	case 3:
		print("Three")
	case _:
		print("Other number")

# Example 3: Match with tuple pattern
point = (0, 5)
match point:
	case (0, y):
		print(f"Y axis at {y}")
	case (x, 0):
		print(f"X axis at {x}")
	case (x, y):
		print(f"Point at ({x}, {y})")

# Example 4: Using guards (if conditions in case)
value = 10
match value:
	case x if x > 0:
		print("Positive number")
	case x if x < 0:
		print("Negative number")
	case _:
		print("Zero")
