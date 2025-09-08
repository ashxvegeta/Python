# Create a list of 5 numbers

# Write a function that returns the sum of squares of that list

# Example: [2, 3, 4] → 2² + 3² + 4² = 29


def fun(nums):
    total = 0
    for n in nums:
        total += n ** 2
    return total

nums = [2, 3, 4]
print(fun(nums))