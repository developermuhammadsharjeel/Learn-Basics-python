
# Creating a tuple (tuples are immutable, meaning they cannot be changed after creation)
names = ("Sahrjeel", "Usama", "Ali", "Minahil", "Ayesha", "Junaid")
print(names)  # Print the whole tuple

# Accessing elements by index
print(names[1])  # Output: Usama

# Slicing a tuple (from index 1 to 3, 3 not included)
print(names[1:3])

# .count(): Returns the number of times a value appears in the tuple
print(names.count("Ali"))

# .index(): Returns the index of the first occurrence of a value
print(names.index("Ayesha"))

# Length of tuple
print(len(names))

# Check if an item exists in the tuple
print("Ali" in names)  # Output: True

# Tuples can contain different data types
mixed_tuple = ("Sharjeel", 42, 3.14, True)
print(mixed_tuple)

# Tuples can be nested
nested_tuple = (names, mixed_tuple)
print(nested_tuple)

# Convert tuple to list (to make it mutable)
names_list = list(names)
names_list.append("NewName")
print(names_list)

