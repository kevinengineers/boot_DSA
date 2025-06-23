def bubble_sort(nums):
    swapping = True
    end = len(nums)

    while swapping:
        swapping = False

        for i in range(1, end):
            if nums[i-1] > nums[i]:
                temp = nums[i-1]
                nums[i-1] = nums[i]
                nums[i] = temp
                swapping = True
        end -= 1
    return nums


test_data = [9, 4, 1, 3, 8, 6, 2, 1, 1, 1]
result = bubble_sort(test_data)
print(result)



