# A Python list is an ordered, mutable collection of items (elements can be any type). Lists are indexed from 0 and can grow/shrink at runtime.

# Key properties

# Ordered: preserves insertion order.
# Mutable: you can change elements, add or remove items.
# Heterogeneous: elements can be different types.
# Dynamic: size changes with append/pop/insert/extend.

# x = [4,True,"hi"]
# y = "ho"
# print(x)
# print(len(x), len(y))
# x.append(5)
# x.extend([6,7])
# x.insert(1,"hello")
# print(x.pop())
# print(x.pop(1)) # remove index 1
# print("access "+x[2]) # access the 2nd element
# y = x[:]
# print("copy list "+ str(y)) # copy the list
# print(x)



# A tuple is an ordered, immutable collection of items in Python. Tuples are indexed (0-based), can contain heterogeneous types, and once created their elements cannot be changed.

# Key points

# Ordered: preserves insertion order.
# Immutable: no item assignment, append, pop, etc.
# Heterogeneous: elements can be different types.
# Useful for fixed-size records, dict keys, and multiple-value returns/unpacking.
# Methods: count(), index().

x = (4, True, "hi")
print(x)
print(x[1]) # access the 2nd element
# x[1] = "test" # error: tuples are immutable
# x.append(5) # error: tuples are immutable
print(x)
x = [[], (), [[], [], [3, 4, 5]]]
print(x)
