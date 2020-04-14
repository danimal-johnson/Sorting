# Helper function
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a_ptr = 0
    b_ptr = 0
    print("A has {} elements. B has {} elements.".format(len(arrA), len(arrB)))

    # Step through the entire sorted array.
    for i in range(0, len(merged_arr)):
        print("i={}, a_ptr={}, b_ptr={}".format(
            i, a_ptr, b_ptr))

        # If we've already exhausted all values in array A,
        # use the value in array B.
        if a_ptr >= len(arrA):
            print("A empty. Using B ({})".format(arrB[b_ptr]))
            merged_arr[i] = arrB[b_ptr]
            b_ptr += 1
            print(merged_arr)

        # Otherwise, if we've already exhausted all the values in array B,
        # get the next value from array A.
        elif b_ptr >= len(arrB):
            print("B empty. Using A ({})".format(arrA[a_ptr]))
            merged_arr[i] = arrA[a_ptr]
            a_ptr += 1
            print(merged_arr)

        # Items remain in both arrays. Compare the first elements and use the lower one.
        else:
            print("Trying a_ptr={}, b_ptr={}".format(a_ptr, b_ptr))
            if a_ptr >= len(a) or b_ptr >= len(b):
                print("This probably shouldn't happen: {}".format(merged_arr))
                continue
            # Use the left array if arrA[0] is lower.
            elif arrA[a_ptr] <= arrB[b_ptr]:
                merged_arr[i] = arrA[a_ptr]
                a_ptr += 1
                print(merged_arr)
            # Use the right array if arrB[0] is lower
            else:
                merged_arr[i] = arrB[b_ptr]
                b_ptr += 1
                print(merged_arr)

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO

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
