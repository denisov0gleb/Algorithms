def bubble_sort(array):
    length = len(array)
    for end_ind in range(length - 1, 0, -1):
        isSorted = True
        for i in range(end_ind):
            if array[i] > array[i + 1]:
                isSorted = False
                array[i], array[i + 1] = array[i + 1], array[i]
        if isSorted:
            break
    return array


def bubble_sort_stupid(array):
    length = len(array)
    for end_ind in range(length - 1, 0, -1):
        for i in range(end_ind):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
    return array


print(bubblesort([1, 7, 5, 3, 0, 3, 10, 5]))
print(bubblesort_stupid([1, 7, 5, 3, 0, 3, 10, 5]))