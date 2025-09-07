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