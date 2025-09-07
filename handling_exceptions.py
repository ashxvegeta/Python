try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.", e)


# finally block
try:
    print(10 / 0)
    
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.", e)
finally:
    print("This will always execute.")