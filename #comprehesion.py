x = [x for x in range(10)]
print(x)
# output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# create a list of numbers from 0 to 9 using list comprehension

print([x+2 for x in range(10)])
# output: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# create a list of numbers from 2 to 11 by adding 2 to each number

print([x%5 for x in range(5)])
# output: [0, 1, 2, 3, 4]

x = [[0 for x in range(10)] for x in range(3)]
print(x)
# output: [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# create a 2D list (3x10) filled with zeros using nested list comprehension

x = [x for x in range(10) if x%2==0]
print(x)
# output: [0, 2, 4, 6, 8]
# create a list of even numbers from 0 to 9 using list comprehension with a condition

x = {i:0 for i in range(5) if i%2==0}
print(x)
# output: {0: 0, 2: 0, 4: 0}
# create a dictionary with even keys from 0 to 4 and values set to 0

x = tuple(x for x in range(5))
print(x)

# test