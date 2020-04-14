# Helper function
def merge(arrA, arrB):
    a_length = len(arrA)
    b_length = len(arrB)
    elements = a_length + b_length
    merged_arr = [0] * elements
    a_ptr = 0
    b_ptr = 0

    # Step through the entire sorted array.
    for i in range(0, len(merged_arr)):
        # If we've already exhausted all values in array A,
        # use the value in array B.
        if a_ptr >= a_length:
            merged_arr[i] = arrB[b_ptr]
            b_ptr += 1
        # Otherwise, if we've already exhausted all the values in array B,
        # get the next value from array A.
        elif b_ptr >= b_length:
            merged_arr[i] = arrA[a_ptr]
            a_ptr += 1
        # Items remain in both arrays. Compare the first elements and use the lower one.
        else:
            if a_ptr >= a_length or b_ptr >= b_length:
                print("This probably shouldn't happen: {}".format(merged_arr))
                continue
            # Use the left array if arrA[0] is lower.
            elif arrA[a_ptr] <= arrB[b_ptr]:
                merged_arr[i] = arrA[a_ptr]
                a_ptr += 1
            # Use the right array if arrB[0] is lower
            else:
                merged_arr[i] = arrB[b_ptr]
                b_ptr += 1

    # print("Merged {} with {} to get {}".format(arrA, arrB, merged_arr))
    return merged_arr


### Merge Sort ###
def merge_sort(arr):
    array_length = len(arr)

    # print("Merge Sorting ", arr)

    if array_length > 1:
        midpoint = int(array_length / 2)
        # print("Midpoint:", midpoint)
        left_array = arr[0:midpoint]
        right_array = arr[midpoint:]
        # print("Left array = {}".format(left_array))
        # print("Right array = {}".format(right_array))
        sorted_left = merge_sort(left_array)
        sorted_right = merge_sort(right_array)
        # sorted_arr = merge(left_array, right_array)
        arr = merge(sorted_left, sorted_right)
        # print("Sorted section:", arr)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr

# Memoization:
# from functools import lru_cache
# @lru_cache(maxsize = 1000) # default = 128


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr


a = [1, 2, 3]
b = [4, 5, 6]
c = [1, 3, 5]
d = [2, 4, 6]
e = [2, 4]
f = [7]
g = [4]
