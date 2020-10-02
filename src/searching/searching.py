def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1  # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    #! Your code here
    if arr == []:
        return -1
    # use to find middle index
    first = 0
    last = len(arr) - 1

    while first <= last:
        # find middle index
        middle = first + last // 2
        if target == arr[middle]:
            return middle
        elif target < arr[middle]:
            last = middle - 1
        elif target > arr[middle]:
            first = middle + 1

    return -1  # not found
