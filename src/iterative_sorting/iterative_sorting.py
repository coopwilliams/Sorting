# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[smallest_index], arr[i] = arr[i], arr[smallest_index]
        print(arr)
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    while True:
        no_swaps = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                no_swaps = False
            print(arr)
        if no_swaps: break
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    counts = [0 for x in range(maximum + 1)]
    for i in arr:
        counts[i] += 1
    running_total = 0
    for pos in range(maximum + 1):
        counts[pos], running_total = running_total, counts[pos] + running_total
    result = [0 for x in range(len(arr))]
    for i in arr:
        result[counts[i]] = i
        counts[i] += 1
    return result

b = [123, 6, 8, 0, 0, 234, 7, 9, 0, 999]
