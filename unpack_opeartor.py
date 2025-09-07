# def func(x):
#     def func2():
#         print(x)
#     return func2
# func(10)()


# arguments unpacking
def funcx(*args, **kwargs):
    pass

x = [1, 23, 22223, 2224]
print(*x)
print(x)


#print using unpacking 

def func3(x,y):
    print(x, y)

pairs = [(1, 2), (3, 4), (5, 6)]
for p in pairs:
    func3(*p)

# dictionaries
def func4(x,y):
    print(x, y)
# print using unpacking dictionaries
pairs = [{'x': 1, 'y': 2}, {'x': 3, 'y': 4}, {'x': 5, 'y': 6}]


# 

# Function that accepts any number of positional and keyword arguments
def func5(*args, **kwargs):
    # *args collects extra positional arguments into a tuple
    # **kwargs collects extra keyword arguments into a dictionary
    print(args, kwargs)

# Call the function with:
# - Positional arguments: 1, 2, 3 → go into args as (1, 2, 3)
# - Keyword arguments: name="John", age=30 → go into kwargs as {"name": "John", "age": 30}
func5(1, 2, 3, name="John", age=30)
