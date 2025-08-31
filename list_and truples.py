# A Python list is an ordered, mutable collection of items (elements can be any type). Lists are indexed from 0 and can grow/shrink at runtime.

# Key properties

# Ordered: preserves insertion order.
# Mutable: you can change elements, add or remove items.
# Heterogeneous: elements can be different types.
# Dynamic: size changes with append/pop/insert/extend.

x = [4,True,"hi"]
y = "ho"
print(x)
print(len(x), len(y))
x.append(5)
x.extend([6,7])
x.insert(1,"hello")
print(x.pop())
print(x.pop(1)) # remove index 1
print("access "+x[2]) # access the 2nd element
y = x[:]
print("copy list "+ str(y)) # copy the list
print(x)