global Value,n
Value = [29, 10, 14, 37, 14, 20, 7, 16, 12]
n = len(Value)

def partition(Value, low, high):
    pivot = Value[low]
    i = low - 1
    j = high + 1

    while (True):
        i += 1
        while (Value[i] < pivot):
            i += 1
        j -= 1
        while (Value[j] > pivot):
            j -= 1
        if (i >= j):
            return j

        Value[i], Value[j] = Value[j], Value[i]


def quickSort(Value, low, high):
    if (low < high):
        pi = partition(Value, low, high)
        quickSort(Value, low, pi)
        quickSort(Value, pi + 1, high)


def printArray(array, n):
    for i in range(n):
        print(array[i], end=" ")
    print()

print("Value = ",Value)
quickSort(Value, 0, n - 1)
print("QuickSort Hoare’s Sorted Array = ",Value)
