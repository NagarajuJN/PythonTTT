my_dict = {'key1': value1, 'key2': value2, 'key3': value3}
empty_dict = {}
nested_dict = {'key1': {'nested_key1': value1, 'nested_key2': value2}, 'key2': value3}
my_dict = {'name': 'Nagaraj', 'age': 25, 'city': 'New York'}
print(my_dict['name'])  # Output: 'Nagaraj'

my_dict['age'] = 26
print(my_dict['age'])  # Output: 26

my_dict['city'] = 'Bangalore'
print(my_dict)  # Output: {'name': Nagaraj, 'age': 25, 'city': 'Bangalore'}

del my_dict['age']
print(my_dict)  # Output: {'name': 'Nagaraj', 'city': 'Bangalore'}
keys_list = list(my_dict.keys())
print(keys_list)  # Output: ['name', 'age']
values_list = list(my_dict.values())
print(values_list)
items_list = list(my_dict.items())
print(items_list) [('name': Nagaraj), ('age': 25), ('city': 'Bangalore')]

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)
print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}

for key in my_dict:
    print(key)
# Output: 'name' 'age'

num_elements = len(my_dict)
print(num_elements)  # Output: 3

my_dict.clear()
print(my_dict)  # Output: {}
