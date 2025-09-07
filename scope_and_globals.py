x = "tim"           # global variable x

def func(name):
    x = name        # creates a NEW local variable x (inside the function scope)

print(x)            # prints the global x → "tim"

func("changed")     # calls the function, assigns local x = "changed"
                    # but this local x exists ONLY inside func and disappears after it ends

print(x)            # still prints the global x → "tim"


# modifying global variable inside a function

x = "time"           # global variable x

def func(name):
    global x        # declare x as global to modify the global variable
    x = name        # modifies the global variable x

print(x)            # prints the global x → "tim"

func("changed")     # calls the function, assigns local x = "changed"
                    # but this local x exists ONLY inside func and disappears after it ends

print(x)            # still prints the global x → "changed"