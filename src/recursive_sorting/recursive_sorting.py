# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    a_count = 0
    b_count = 0
    for i in range(len(arrA)):
        for j in range(b_count, len(arrB)):
            if arrA[i] <= arrB[j]:
                merged_arr[a_count + b_count] = arrA[i]
                a_count += 1
                break
            else:
                merged_arr[a_count + b_count] = arrB[j]
                b_count += 1
    if b_count < len(arrB):
        merged_arr[a_count + b_count:] = arrB[b_count:]
    if a_count < len(arrA):
        merged_arr[a_count + b_count:] = arrA[a_count:]
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) <= 1:
        return arr
    midpoint = len(arr)//2
    arr = merge(merge_sort(arr[:midpoint]), merge_sort(arr[midpoint:]))
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    
    return arr

def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr


a = [0, 3, 5, 77, 111]
b = [0, 1, 2, 3, 88, 99, 1111, 345345]
c = [756, 9, 12, 0, 90, 0, 13 , 6]
