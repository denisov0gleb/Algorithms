def selection_sort(array):
    """
    Selection sort
    Complexity: always O(n^2)
    """
    length = len(array)
    for start_ind in range(length - 1):
        max_value_ind = 0
        for i in range(length - start_ind):
            if array[i] > array[max_value_ind]:
                max_value_ind = i
        array[i], array[max_value_ind] = array[max_value_ind], array[i]
    return array


print(selection_sort([1, 7, 5, 3, 0, 3, 10, 5]))