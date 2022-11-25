global array
array = [29, 10, 14, 37, 14, 20, 7, 16, 12]

def Mergesort(Value):
    if len(Value) > 1:
        mid = len(Value) // 2
        left = Value[:mid]
        right = Value[mid:]

        Mergesort(left)
        Mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                Value[k] = left[i]
                i += 1
            else:
                Value[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            Value[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            Value[k] = right[j]
            j += 1
            k += 1

print("Array = ",array)
Mergesort(array)
print("MergeSort Sorted Array = ",array)
