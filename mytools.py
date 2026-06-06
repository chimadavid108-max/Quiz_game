def line():
    divider = "-" * 40
    print(divider)
    return divider

def add(*nums):
    return sum(nums)

def minus(*nums):
    if not nums: return 0
    res = nums[0]
    for i in nums[1:]:
        res -= i
    return res

def multiply(*nums):
    if not nums: return 0
    res = 1
    for i in nums:
        res *= i
    return res

def divide(*nums):
    if not nums: return 0
    res = nums[0]
    for i in nums[1:]:
        if i == 0:
            print("Error: Division by zero")
            return None
        res /= i
    return res
