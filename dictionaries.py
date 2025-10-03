

# Dictionaries in Python:
# - Unordered collections of key-value pairs
# - Keys must be unique and immutable (e.g., strings, numbers, tuples)
# - Values can be of any type
# - Mutable (can add, remove, or change items)

# Creating a dictionary
dictlist = {"Color": "Red", "Model": 2021, "Brand": "Ferrari", "Car": "Ferrari 486 Spider"}

# Accessing a value by key
print(dictlist["Car"])  # Output: Ferrari 486 Spider

# .get(): Access value by key, returns None (or default) if key not found
print(dictlist.get("Brand"))
print(dictlist.get("Owner", "Not specified"))

# .keys(): Get all keys
print(dictlist.keys())

# .values(): Get all values
print(dictlist.values())

# .items(): Get all key-value pairs as tuples
print(dictlist.items())

# .update(): Update dictionary with another dictionary or key-value pairs
dictlist.update({"Owner": "Sharjeel"})
print(dictlist)

# .pop(): Remove item by key and return its value
removed = dictlist.pop("Model")
print("Removed Model:", removed)
print(dictlist)

# .popitem(): Remove and return the last inserted key-value pair
last_item = dictlist.popitem()
print("Popped item:", last_item)
print(dictlist)

# .setdefault(): Get value of key, set it if not present
print(dictlist.setdefault("Country", "Pakistan"))
print(dictlist)

# .copy(): Make a shallow copy of the dictionary
dict_copy = dictlist.copy()
print("Copied dict:", dict_copy)

# .clear(): Remove all items from the dictionary
dict_copy.clear()
print("Cleared dict:", dict_copy)

# Looping through keys and values
for key, value in dictlist.items():
	print(f"Key: {key}, Value: {value}")