def binary_search(target, arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        median = (low + high) // 2

        if arr[median] == target:
            return True
        elif arr[median] < target:
            low = median + 1
        else:
            high = median - 1
    
    return False


dataset = [1, 2, 3, 4, 5]
test = binary_search(4, dataset)
print(test)
