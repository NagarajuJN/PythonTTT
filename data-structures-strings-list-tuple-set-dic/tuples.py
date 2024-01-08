empty_tuple = ()
single_element_tuple = ("python",)

fruits = ("apple", "banana", "orange")
second_fruit = fruits[1]
print(second_fruit)# Retrieves "banana"

numbers = (1, 2, 3, 4, 5)
subset = numbers[1:4]
print(subset)# Retrieves (2, 3, 4)

name = "Alice"
age = 30
person = name, age
print(person)# Tuple packing

colors = ("red", "yellow")
combo = fruits + colors  # Concatenates tuples

weather_data = (25, 72, 0.2)
del weather_data  # Deletes the entire tuple

fruits = ("apple", "banana", "orange")
for fruit in fruits:
    print(fruit)

# Tuple Methods and Operations

numbers = (1, 2, 2, 3, 2, 4, 2, 5)
twos_count = numbers.count(2)  # 2
colors = ("red", "green", "blue")
green_index = colors.index("green") #1
