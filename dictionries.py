# A dictionary (often misspelled "dictionries") is an unordered, mutable mapping from hashable keys to values in Python.

# Key points

# Mapping: key -> value pairs.
# Keys must be hashable (strings, numbers, tuples).
# Values can be any type and can repeat.
# Mutable: add/update/remove entries.
# Fast membership test for keys.
# Common methods

# d[key], d.get(key, default)
# d.keys(), d.values(), d.items()
# d.update(other), d.setdefault(key, default)
# d.pop(key), d.popitem()
# dict(), dict.fromkeys(), comprehensions


x = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(x['name']);
print(x['age']);
print(x['city']);   


# output: Alice
# output: 30
# output: New York

x['key2'] = 31
print(x)
# output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'key2': 31}
# add key2 with value 31 to the dictionary

x[2] = 8
print(x)

# output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'key2': 31, 2: 8}
# add key 2 with value 8 to the dictionary

x[3] = [1,2,3]
print(x)
# output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'key2': 31, 2: 8, 3: [1, 2, 3]}
# add key 3 with value [1,2,3] to the dictionary

print('name' in x)
# output: True

print(list(x.values()))
# output: ['Alice', 30, 'New York', 31, 8, [1, 2, 3]]
# get all values in the dictionary
print(list(x.keys()))
# output: ['name', 'age', 'city', 'key2', 2, 3]
# get all keys in the dictionary

del x['key2']
print(x)
# output: {'name': 'Alice', 'age': 30, 'city': 'New York', 2: 8, 3: [1, 2, 3]}
# delete key2 from the dictionary


for key, value in x.items():
    print(f"{key}: {value}")
# output:
# name: Alice
# age: 30
# city: New York
# 2: 8
# 3: [1, 2, 3]
# iterate over key-value pairs in the dictionary
# Note: Dictionaries maintain insertion order as of Python 3.7+.