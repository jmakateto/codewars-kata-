def find_smallest_sorted_subarray(arr):
    n = len(arr)

    # If all elements are the same, or array is already sorted, return [0, 0]
    if all(x == arr[0] for x in arr) or arr == sorted(arr) or arr == sorted(arr, reverse=True):
        return [0, 0]

    # Find the left boundary of the unsorted subarray
    m = 0
    while m < n - 1 and arr[m] <= arr[m + 1]:
        m += 1

    # Find the right boundary of the unsorted subarray
    n = len(arr) - 1
    while n > 0 and arr[n] >= arr[n - 1]:
        n -= 1

    # Find the min and max within the unsorted subarray
    subarray_min = min(arr[m:n + 1])
    subarray_max = max(arr[m:n + 1])

    # Expand the left boundary if needed
    while m > 0 and arr[m - 1] > subarray_min:
        m -= 1

    # Expand the right boundary if needed
    while n < len(arr) - 1 and arr[n + 1] < subarray_max:
        n += 1

    return [m, n]

#  usage:
arr = [1, 2, 3, 6, 4, 4]
result = find_smallest_sorted_subarray(arr)
print(result)  
# result: [3, 5]
