global array
array = [29, 10, 14, 37, 14, 20, 7, 16, 12]

def partition(array, low, high):
    pivot = array[high]

    i = low - 1
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
    temp = array[i + 1]
    array[i + 1] = array[high]
    array[high] = temp
    return i + 1

def quicksort(array, low, high):
    if low < high:
        p = partition(array, low, high)
        quicksort(array, low, p - 1)
        quicksort(array, p + 1, high)
    return array

def Quicksort(array):
    return quicksort(array, 0, len(array) - 1)

print("Array = ",array)
Quicksort(array)
print("Lomuto QuickSort Sorted Array = ",array)
