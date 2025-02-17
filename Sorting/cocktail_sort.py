def cocktail_sort(array):
    """
    Cocktail sort
    Complexity: 
                - worst case O(n^2)
                - best case O(n)
                - average case O(n^2)
    """
    length = len(array)
    for start_ind in range(0, length//2+1):
        max_value_ind = start_ind
        min_value_ind = start_ind
        for i in range(start_ind, length - 1 - start_ind):
            if array[i] >= array[max_value_ind]:
                max_value_ind = i
            if array[i] < array[min_value_ind]:
                min_value_ind = i
        array[length - start_ind - 1], array[max_value_ind] = array[max_value_ind], array[length - start_ind - 1]
        array[start_ind], array[min_value_ind] = array[min_value_ind], array[start_ind]
    return array


print(cocktail_sort([1, 7, 5, 3, 0, 3, 10, 5]))