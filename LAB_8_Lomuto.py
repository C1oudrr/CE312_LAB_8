global Value
Value = [29, 10, 14, 37, 14, 20, 7, 16, 12]

def partition(Value, low, high):
    pivot = Value[high]

    i = low - 1
    for j in range(low, high):
        if Value[j] < pivot:
            i += 1
            temp = Value[i]
            Value[i] = Value[j]
            Value[j] = temp
    temp = Value[i + 1]
    Value[i + 1] = Value[high]
    Value[high] = temp
    return i + 1

def quicksort(array, low, high):
    if low < high:
        p = partition(array, low, high)
        quicksort(array, low, p - 1)
        quicksort(array, p + 1, high)
    return array

def Quicksort(Value):
    return quicksort(Value, 0, len(Value) - 1)

print("Value = ",Value)
Quicksort(Value)
print("Lomuto QuickSort Sorted Array = ",Value)
