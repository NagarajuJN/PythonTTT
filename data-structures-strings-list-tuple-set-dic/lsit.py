my_list = [1, 2, 'orange', 44.5]
print(my_list)
Output:
[1, 2, 'orange', 44.5]


# Creating an integer list
integer_list = [1, 2, 3, 4, 5]
print(integer_list)

# Creating a float list
float_list = [1.2, 2.3, 3.4, 4.5, 5.6]
print(float_list)

# Creating a string list
string_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(string_list)

# integer_list
[1, 2, 3, 4, 5]

# float_list
[1.2, 2.3, 3.4, 4.5, 5.6]

# string_list
['apple', 'banana', 'cherry', 'date', 'elderberry']

# Accessing the items in List
my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(my_list[0])
print(my_list[2])
Output:
apple
cherry

two_dim_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(two_dim_list[0][1])

two_dim_list_str = [["apple", "banana", "cherry"], ["dog", "cat", "mouse"]]
print(two_dim_list_str[1][0])
Output:
2
dog


# Slicing of a List
num_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Slicing from index 2 to 5 (exclusive)
print(num_list[2:5])   # Output: [30, 40, 50]

# Slicing from the start to index 3 (exclusive)
print(num_list[:3])    # Output: [10, 20, 30]

# Slicing from index 6 to the end
print(num_list[6:])    # Output: [70, 80, 90, 100]

# Slicing the last three items
print(num_list[-3:])   # Output: [80, 90, 100]

# Slicing every second item
print(num_list[::2])   # Output: [10, 30, 50, 70, 90]
Output:


[30, 40, 50]

[10, 20, 30]

[70, 80, 90, 100]

[80, 90, 100]

[10, 30, 50, 70, 90]

# Updating a List

my_list_1 = ['apple', 'banana', 'cherry']
my_list[1] = 'blackberry'
print(my_list)

my_list_2 = ['apple', 'banana', 'cherry', 'date', 'elderberry']
my_list[1:3] = ['blackberry', 'citrus']
print(my_list)
Output:


['apple', 'blackberry', 'cherry']

['apple', 'blackberry', 'citrus', 'date', 'elderberry']

# Method on list:

my_list = ['apple', 'banana', 'cherry']
my_list.append('date')
print(my_list)
Output:
['apple', 'banana', 'cherry', 'date']

my_list.insert(1, 'banana')
print(my_list)
Output:
['apple', 'banana', 'cherry', 'date']
my_list.extend(['date', 'elderberry'])
print(my_list)
Output:
['apple', 'banana', 'cherry', 'date', 'elderberry']

my_list.remove('banana')
print(my_list)
Output:
['apple', 'cherry']

my_list.pop(1)
print(my_list)
Output:


['apple', 'cherry']
del my_list[1]
print(my_list)
Output:


['apple', 'cherry']
del my_list[1:3]  print(my_list)

# delete entire list
del my_list
Output:


['apple', 'date', 'elderberry']

my_list = ['apple', 'banana', 'cherry']
for item in my_list:
    print(item)
Output:


apple
banana
cherry

# List comprehension


# Example 1: Squares of all numbers in the list
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print(squares)

# Example 2: Squares of numbers greater than 2 in the list
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers if n > 2]
print(squares)
Output:


[1, 4, 9, 16, 25]

9, 16, 25]

