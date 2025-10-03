
# Sets in Python:
# - Unordered collections of unique elements (no duplicates)
# - Mutable (can add/remove items)
# - Elements must be immutable (e.g., numbers, strings, tuples)
# - No indexing or slicing (unlike lists/tuples)

# Creating a set
setslist = {"Noman", "ali", "Junaid", "kamran", "huzaifa", "Moazzam", "Rashid", "Ahmad Raza"}
print(setslist)  # Print the set (order is not guaranteed)

# Adding an element
setslist.add("NewName")
print("After add:", setslist)

# Removing an element (raises KeyError if not found)
setslist.remove("ali")
print("After remove:", setslist)

# Discarding an element (no error if not found)
setslist.discard("NotInSet")

# .pop(): Remove and return a random element
popped = setslist.pop()
print("Popped element:", popped)
print("After pop:", setslist)

# .clear(): Remove all elements
copy_set = setslist.copy()
copy_set.clear()
print("Cleared set:", copy_set)

# Set operations
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}

# Union: all unique elements from both sets
print("Union:", setA.union(setB))

# Intersection: elements common to both sets
print("Intersection:", setA.intersection(setB))

# Difference: elements in setA but not in setB
print("Difference:", setA.difference(setB))

# Symmetric difference: elements in either set, but not both
print("Symmetric Difference:", setA.symmetric_difference(setB))

# Check membership
print(3 in setA)  # True

# Length of set
print(len(setA))