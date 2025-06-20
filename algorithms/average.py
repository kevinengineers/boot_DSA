def average_followers(nums):

    #Can't divide by zero.
    if len(nums) == 0:
        return None

    average = 0
    divisor = len(nums)

    for num in nums:
        average += num

    return average / divisor
