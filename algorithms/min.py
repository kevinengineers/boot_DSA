def find_minimum(nums):
    min = float("inf")

    if len(nums) == 0:
        return None
    for num in nums:
        if num < min:
            min = num
    return min

print(find_minimum([1, 2, 3, 4, 5]))
print(find_minimum([4, 7, 3, 9, -50]))

"""
Set minimum to positive infinity: float("inf").
If the list is empty, return None.
For each number in the list nums, compare it to minimum. If the number is smaller than minimum, set minimum to that number.
minimum is now set to the smallest number in the list. Return it.
"""
