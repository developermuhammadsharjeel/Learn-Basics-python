## Simple Text (string)

name = "Sharjeel"
print(name)



"""
Multiline Strings: Used to print a paragraph in a single output.
It's a very awesome feature of Python.
"""


paragraph = """     This is a paragraph. In this way, we can create and print multiline strings.
We can add any type of text and paragraph in this area. Simply, we have to write the paragraph within three double quotes so
we can print it.
"""
print(paragraph)


# .upper() to convert all characters of text to upper case
print(paragraph.upper())

# .lower() to convert all text to lower case
print(paragraph.lower())

# .capitalize() to capitalize the first character
print(paragraph.capitalize())

# .title() to capitalize the first letter of each word
print(paragraph.title())

# .swapcase() to swap case of all characters
print(paragraph.swapcase())

# .casefold() for aggressive lowercasing (useful for case-insensitive comparisons)
print(paragraph.casefold())

# .replace() to replace a specific text
print(paragraph.replace("This is a paragraph", "This is a simple paragraph"))

# .strip() to remove whitespace from start and end
print(paragraph.strip())

# .lstrip() to remove whitespace from the start only
print(paragraph.lstrip())

# .rstrip() to remove whitespace from the end only
print(paragraph.rstrip())

# .split() to separate text into a list by whitespace (default)
print(paragraph.split())

# .splitlines() to split at line breaks
print(paragraph.splitlines())

# .join() to join a list of strings with a separator
words = ["Hello", "World"]
print(" ".join(words))

# .find() to find the first occurrence of a substring, returns -1 if not found
print(paragraph.find("paragraph"))

# .rfind() to find the last occurrence of a substring
print(paragraph.rfind("paragraph"))

# .index() to find the first occurrence, raises ValueError if not found
try:
	print(paragraph.index("paragraph"))
except ValueError:
	print("Not found")

# .count() to count occurrences of a substring
print(paragraph.count("paragraph"))

# .startswith() to check if string starts with a substring
print(paragraph.startswith("This"))

# .endswith() to check if string ends with a substring
print(paragraph.endswith("it."))

# .isalpha() to check if all characters are alphabetic
print(name.isalpha())

# .isdigit() to check if all characters are digits
print(name.isdigit())

# .isalnum() to check if all characters are alphanumeric
print(name.isalnum())

# .isspace() to check if all characters are whitespace
print(paragraph.isspace())

# .islower() to check if all characters are lowercase
print(paragraph.islower())

# .isupper() to check if all characters are uppercase
print(paragraph.isupper())

# .istitle() to check if string is titlecased
print(paragraph.istitle())

# .zfill(width) to pad string on the left with zeros
num = "42"
print(num.zfill(5))

# .center(width, fillchar) to center string
print(name.center(20, '-'))

# .ljust(width, fillchar) to left-justify string
print(name.ljust(20, '*'))

# .rjust(width, fillchar) to right-justify string
print(name.rjust(20, '*'))

# .partition() to split string at first occurrence of separator
print(paragraph.partition("paragraph"))

# .rpartition() to split string at last occurrence of separator
print(paragraph.rpartition("paragraph"))

# .encode() to encode string to bytes
print(name.encode())



