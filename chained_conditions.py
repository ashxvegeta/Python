x = 7
y = 10
z = 5

result1 = x == y 
result2 = y > x
result3 = z < x+2

final_result = result1 or result2  or result3
print(final_result)  # True
print(not final_result)  # False        
print(not(False and True or True))  # False