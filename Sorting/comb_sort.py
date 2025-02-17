def comb_sort(array):
    """
    Comb sort
    Complexity: 
                - worst case O(n^2)
                - best case O(n * log n)
                - average case O(n^2)
    """
    length = len(array)
    step = length * 3 // 4
    isSwapped = False
    while step > 1 or isSwapped:
        if step > 1:
            step = step * 3 // 4
        i = 0
        isSwapped = False
        while i + step < length:
            if array[i] > array[i + step]:
                array[i], array[i + step] = array[i + step], array[i]
                isSwapped = True
            i += step
    return array


print(comb_sort([1, 7, 5, 3, 0, 3, 10, 5]))