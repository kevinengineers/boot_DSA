def find_max(nums):
    max = float("-inf")
    for num in nums:
        if num > max:
            max = num
    return max


# Testing
test1 = find_max([1, 2, 3, 4, 5])
test2 = find_max([5, 8, 1, 0, -99])
print(f"test1: {test1}")
print(f"test2: {test2}")


