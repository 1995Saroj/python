def mergeSort(data):
    print("Splitting ",data)
    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1
    
        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1
    
        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1

    print("Merging ",data)
    
data = [14,46,43,27,57,41,45,21,70]
mergeSort(data)
print(data)