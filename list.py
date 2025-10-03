


# Creating a list of fruits
thislist = ["apple", "Banana", "Strawberry", "orange", "Pineapple"]
print(thislist)  # Print the whole list

# Get the number of items in the list
print(len(thislist))  # Output: 5

# Accessing an item by index (indexing starts from 0)
print(thislist[2])  # Output: Strawberry

# List with multiple types of data (string, int, bool, float)
listw = ["Name", 98, True, 99.9, "Sharjeel"]
print(listw)

# Slicing: get items from index 1 to 4 (5 is not included)
print(listw[1:5])

# .append(): Add an item to the end of the list
listw.append(98)
print(listw)

# .insert(): Insert an item at a specific position
listw.insert(1, "Inserted")
print(listw)

# .remove(): Remove the first occurrence of a value
listw.remove(98)
print(listw)

# .pop(): Remove and return item at given index (default last)
removed_item = listw.pop()
print("Popped item:", removed_item)
print(listw)

# .clear(): Remove all items from the list
copy_list = listw.copy()  # Copy for demonstration
copy_list.clear()
print("Cleared list:", copy_list)

# .index(): Get the index of the first occurrence of a value
print("Index of 'Name':", listw.index("Name"))

# .count(): Count occurrences of a value
print("Count of True:", listw.count(True))

# .reverse(): Reverse the list in place
listw.reverse()
print("Reversed list:", listw)

# .sort(): Sort the list (works if all items are of comparable types)
num_list = [5, 2, 9, 1, 5]
num_list.sort()
print("Sorted num_list:", num_list)

# .copy(): Make a shallow copy of the list
new_list = thislist.copy()
print("Copied list:", new_list)

# .extend(): Add all items from another list
new_list.extend(["Mango", "Grapes"])
print("Extended list:", new_list)





