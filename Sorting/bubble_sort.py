def bubble_sort(array):
    """
    Bubble sort with a flag
    Complexity: 
                - worst case O(n^2)
                - best case O(n)
                - average case O(n^2)
    """
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
    """
    Stupid Bubble sort
    Complexity: always O(n^2)
    """
    length = len(array)
    for end_ind in range(length - 1, 0, -1):
        for i in range(end_ind):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
    return array


print(bubble_sort([1, 7, 5, 3, 0, 3, 10, 5]))
print(bubble_sort_stupid([1, 7, 5, 3, 0, 3, 10, 5]))