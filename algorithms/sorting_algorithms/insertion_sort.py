def insertion_sort(nums):
    i = 1
    while i < len(nums):
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            temp = nums[j - 1]
            nums[j - 1] = j
            nums[j] = temp
            print(nums)
            j -= 1
        i += 1
    return nums
