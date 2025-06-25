def merge_sort(nums):
    if len(nums) < 2:
        return nums
    part = len(nums) // 2
    left_list = nums[:part]
    right_list = nums[part:]    
    sorted_left = merge_sort(left_list)
    sorted_right = merge_sort(right_list)

    return merge(sorted_left, sorted_right)
    

def merge(first, second):
    final = []
    while first and second:
        if first[0] < second[0]:
           final.append(first.pop(0))
        else:
            final.append(second.pop(0))
    
    if first:
        final.extend(first)
    elif second:
        final.extend(second)

    return final


data = [2, 1, 3, 4, 9, 5, 84]

res = merge_sort(data)
print(f"result: {res}")
