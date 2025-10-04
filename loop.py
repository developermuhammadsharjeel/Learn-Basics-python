# Loops in Python
# ----------------
# Loops are used to execute a block of code repeatedly.
# Python has two main types of loops: for loop and while loop.

# 1. for loop: Used to iterate over a sequence (like list, tuple, string, etc.)
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
	print(fruit)
# Output: apple\nbanana\ncherry

# 2. while loop: Repeats as long as a condition is True
count = 0
while count < 3:
	print("Count is:", count)
	count += 1
# Output: Count is: 0\nCount is: 1\nCount is: 2

# You can use break to exit a loop early
for i in range(5):
	if i == 3:
		break
	print(i)
# Output: 0\n1\n2

# You can use continue to skip to the next iteration
for i in range(5):
	if i == 2:
		continue
	print(i)
# Output: 0\n1\n3\n4
