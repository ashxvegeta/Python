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