def quick_sort(nums, low, high):
    if low < high:
        middle = partition(nums, low, high)
        quick_sort(nums, low, middle - 1)
        quick_sort(nums, middle + 1, high)


def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1
    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
    temp = nums[i + 1]
    nums[i + 1] = pivot
    nums[high] = temp
    return i + 1


test_data = [9, 4, 6, 3, 7, -3, 99, 2, 54]
print(f"test data before: {test_data}")
quick_sort(test_data, 0, len(test_data) - 1)
print(test_data)
