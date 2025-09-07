x = [1, 2, 3, 4, 5]
y = list(map(lambda a: a + 10, x))
print(y)
# output: [11, 12, 13, 14, 15]


# filter
z = list(filter(lambda a: a % 2 == 0, x))
print(z)
# output: [2, 4]
# getting  only even numbers from using filter function