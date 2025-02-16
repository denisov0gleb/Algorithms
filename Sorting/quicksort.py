def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        less_array = []
        greater_array = []
        middle_array = []
        middle_ind = len(array) // 2
        for item in array:
            if item < array[middle_ind]:
                less_array.append(item)
            elif item > array[middle_ind]:
                greater_array.append(item)
            else:
                middle_array.append(item)
        return quicksort(less_array) + middle_array + quicksort(greater_array)


def quicksort_bad(array):
  if len(array) < 2:
    return array
  else:
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([1, 7, 5, 3, 0, 3, 10, 5]))
print(quicksort_bad([1, 7, 5, 3, 0, 3, 10, 5]))