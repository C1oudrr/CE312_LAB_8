global array,n
array = [29, 10, 14, 37, 14, 20, 7, 16, 12]
n = len(array)

def partition(array, low, high):
    pivot = array[low]
    i = low - 1
    j = high + 1

    while (True):
        i += 1
        while (array[i] < pivot):
            i += 1
        j -= 1
        while (array[j] > pivot):
            j -= 1
        if (i >= j):
            return j

        array[i], array[j] = array[j], array[i]


def quickSort(array, low, high):
    if (low < high):
        pi = partition(array, low, high)
        quickSort(array, low, pi)
        quickSort(array, pi + 1, high)


def printArray(array, n):
    for i in range(n):
        print(array[i], end=" ")
    print()

print("Array = ",array)
quickSort(array, 0, n - 1)
print("QuickSort Hoare’s Sorted Array = ",array)
