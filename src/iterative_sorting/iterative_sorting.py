
def selection_sort(arr):
    # Ignore arrays that are too short.
    if len(arr) <= 1:
        return arr

    # Loop through n-1 elements using i
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # Find next smallest element on the right
        # of index i using cur_index
        for cur_index in range(i+1, len(arr)):
            if arr[cur_index] < arr[smallest_index]:
                smallest_index = cur_index

        # If a smaller value was found to the right, swap it with
        # the current value.
        if smallest_index != i:
            temp = arr[i]
            arr[i] = arr[smallest_index]
            arr[smallest_index] = temp

        #     print("Swapping {}({}) with {}({}): {}".format(
        #         i, arr[i], smallest_index, arr[smallest_index], arr))
        # else:
        #     print("Skipping element {} ({})".format(
        #         i, arr[i]))

    return arr


def bubble_sort(arr):
    # Ignore arrays that are too short
    if len(arr) <= 1:
        return arr

    # Make 1 pass (p) for every element in the array.
    for p in range(1, len(arr) - 1):
        # print("checking from 0 to {}".format(len(arr) - p))
        swaps_made = False

        # The END of the list is sorted after each pass,
        # so we subract p each time to get a shorter list.
        for i in range(0, len(arr) - p):

            # print("{}: arr[{}] = {}".format(arr, i, arr[i]))

            # Start at index 0. Compare neighbors and swap larger
            # items to the right until they "bubble" up to the end
            # of the list.
            if arr[i] > arr[i+1]:  # Swap
                swaps_made = True
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
        # Once we make a pass without any swaps, the list is sorted.
        if swaps_made == False:
            return arr

    print("Error: Things didn't go as planned")
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
