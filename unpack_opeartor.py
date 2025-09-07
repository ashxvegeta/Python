def func(x):
    def func2():
        print(x)
    return func2
func(10)()