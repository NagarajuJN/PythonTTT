# Strings in Python

name = 'John Doe'
message = "Hello, World!"
multiline_string = '''This is a
multiline
string.'''


# Basic Operations with Strings

# Concatenation
first_name = 'Nagaraj'
last_name = 'JN'
full_name = first_name + last_name
print(full_name)

# Output: NagarajuJN

 # Indexing and Slicing
greeting = 'Hello, World!'
print(greeting[0])        # Output: H
print(greeting[7:12])     # Output: World
print(greeting[:5])       # Output: Hello
print(greeting[-6:])      # Output: World!


text = "Hello"
print(text[2:1])  # o/p an empty string
print(text[:])    # o/p whole string

text = "Hello"
print(text[1:4:0])  # o/p ValueError
print(text[4:1:-1]) # o/p This will work and return "oll"

text = "Hello"
text[0] = "h"  # o/p result in an error due to immutability

number = 12345
print(number[2])  # o/p   a TypeError

# Length of a String:

message = "Python is amazing!"
length = len(message)
print(length)  # Output: 19


# String Methods and Functions

  # String Methods

  # ‘find()’ and ‘index()’:
text = "Python is very easy"
print(text.find("is"))     # Output: 7
print(text.index("is"))    # Output: 7

# ‘replace()’:
message = "Hello, World!"
new_message = message.replace("Hello", "Nagaraj")
print(new_message)     # Output: Nagaraj, World!

# strip()’, ‘lstrip()’, and ‘rstrip()’:
text = "   Hello, World!   "
x = text.strip()
print(x)  # Output: "Hello, World!"
x = text.lstrip()
print(x)  # Output: "Hello, World!"
x = text.rstrip()
print(x)  # Output: "Hello, World!"




# upper() and lower():

text = "Nagaraj!"
print(text.upper())   # Output: NAGARAJ
print(text.lower())   # Output: nagaraj

sentence = "Python is easy to learn and Python is versatile."
index = sentence.find("Python") # Output 0

sentence = "Python is easy to learn and Python is versatile."
count = sentence.count("Python") # 2


text = "Hello, World!"
starts_with_hello = text.startswith("Hello") # True
ends_with_world = text.endswith("world") # False

word = "Python123"
is_alpha = word.isalpha() # False (contains digits)
is_digit = word.isdigit() # False (contains letters)

str1 = "apple"
str2 = "apple"
result = str1 == str2 # True

 # String Formatting
name = "Nagaraj"
age = 25
message = "My name is {} and I am {} years old.".format(name, age)
print(message)  # Output: My name is Nagaraj and I am 25 years old.

input_string = "Nagaraj123"
result_string = ''
for char in input_string:
    if not char.isdigit():
result_string += char
print(result_string) # Output: "Nagaraj"

# program in python to remove spaces from a given string
def remove_spaces(input_string):
    # Use the replace() function to remove spaces
    result_string = input_string.replace(" ", "")
    return result_string

# Example usage:
input_string = "Hello, this is a test string with spaces"
result = remove_spaces(input_string)
print("Original String:", input_string)
print("String after removing spaces:", result)
