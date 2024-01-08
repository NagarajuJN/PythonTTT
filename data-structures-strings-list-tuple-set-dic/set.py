my_set = {1, 2, 3}

# Using the set() constructor
another_set = set([3, 4, 5])

# Creating an empty set
empty_set = set()

# Looping through a set
for item in my_set:
    print(item)

# Set Methods and Built-in Functions
# Copying a set
new_set = my_set.copy()

# Updating a set with the difference of another set
my_set.difference_update(another_set)

# Checking if sets have no common elements
is_disjoint = my_set.isdisjoint(another_set)

# Getting the length, maximum, and minimum elements
length = len(my_set)
max_element = max(my_set)
min_element = min(my_set)

# Set Comprehensions

squared_set = {x**2 for x in range(10)}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_result = set1.intersection(set2) # or set1 & set2
union_result = set1.union(set2) # or set1 | set2
difference_result = set1.difference(set2) # or set1 - set2
symmetric_difference_result = set1.symmetric_difference(set2) # or set1 ^ set2
is_subset = set2.issubset(set1) # True, set2 is a subset of set1
is_superset = set1.issuperset(set2) # True, set1 is a superset of set2
