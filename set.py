
# A set in Python is an unordered collection of unique, hashable elements. Use it when you need membership tests, deduplication, or set math.

# Key points

# Unordered: no index, iteration order is arbitrary.
# Unique: duplicates are removed.
# Elements must be hashable (immutable types like numbers, strings, tuples).
# Mutable: you can add/remove elements (use frozenset for an immutable set).
# Common ops: add, remove, discard, pop, union, intersection, difference, symmetric_difference, issubset, issuperset.


s = {4,32,2,2}
print(s)
# output: {32, 2, 4}
# duplicates are removed and the order is not guaranteed
s.add(5)
print(s)
# output: {32, 2, 4, 5}
# add 5 to the set
s.remove(2)
print(s)
# output: {32, 4, 5}
# remove 2 from the set
print(4 in s)
# output: True
# check if 4 is in the set
print(10 in s)
# output: False
# check if 10 is in the set

s2 = {4,5,6,7}
print(s.union(s2))
# output: {32, 2, 4, 5, 6, 7}
# union of two sets
print(s.intersection(s2))
# output: {4, 5}
# intersection of two sets