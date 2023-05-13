def index_equals_value_search(arr):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] - mid < 0:
            start = mid+1
        else:
            if arr[mid] - mid == 0 and ((mid == 0) or (arr[mid-1] - (mid-1) < 0)):
                return mid
            else:
                end = mid-1
    return -1


print(index_equals_value_search([-8, 0, 2, 5]))
# print(index_equals_value_search([-6, -5, -4, -1, 1, 3, 5, 7]))
print(index_equals_value_search([-5, 0, 2, 5, 7, 10, 29]))
