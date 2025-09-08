# 📌 Your Task 2:
# Try modifying this function to return the average of squares instead of the sum.

# 👉 Hint: average = (sum of squares) / (length of list).

def fun(nums):
    total = 0
    length = len(nums)
    for n in nums:
        total += n ** 2
    return total / length

nums = [1, 2, 3, 4, 5]
print(fun(nums))