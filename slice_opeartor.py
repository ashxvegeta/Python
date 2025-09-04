x = [0,1,2,3,4,5,6,7,8,9]
y = ['hi','hello','howdy','greetings']
s = "Hello World"

sliced = x[0:5]
# print(sliced)
# output: [0, 1, 2, 3, 4]

sliced = x[0:4:2]
# print(sliced)
# output: [0, 2]
# start with 0 go to 2 and then go to 4 since 4 is the stop we will not include the 4

sliced = x[:2]
print("start with 0 go to 1 since 2 is the stop we will not include the 2")
print(sliced)
# output: [0, 1]
# start with 0 go to 1 since 2 is the stop we will not include the 2

sliced = x[2:4]
print("start with 2 go to 3 since 4 is the stop we will not include the 4")
print(sliced)
# output: [2, 3]
# start with 2 go to 3 since 4 is the stop we will not include the 

sliced = x[4:2:-1]
print("start with 4 go to 3 and then go to 2 since 2 is the stop we will not include the 2")
print(sliced)
# output: [4, 3]
# start with 4 go to 3 and then go to 2 since 2 is the stop we will not include the 2

sliced = x[::-1]
print("start with 9 go to 8 then 7 then 6 then 5 then 4 then 3 then 2 then 1 then 0 since -1 is the stop we will not include the -1")
print(sliced)
# output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# start with 9 go to 8 then 7 then 6 then 5 then 4 then 3 then 2 then 1 then 0 since -1 is the stop we will not include the -1

stringsliced = s[::2]
print(stringsliced)
# output: HloWrd
# start with 0 go to 1 then 2 then 3 then 4 since 5 is the stop we will not include the 5
