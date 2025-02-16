def array_len(array):
    if array:
        return 1 + array_len(array[1:])
    else:
        return 0

def array_sum(array):
    if not array:
        return 0
    else:
        return array[0] + array_sum(array[1:])
    
def array_mean(array):
    if not array:
        return None
    elif len(array) == 1:
        return array[0]
    else:
        return (array[0] + array_mean(array[1:]) ) / 2
    
def array_max(array):
    if not array:
        return None
    elif len(array) == 1:
        return array[0]
    else:
        max_item = array_max(array[1:])
        if array[0] > max_item:
            max_item = array[0]
        return max_item
    
    
print(array_len([1, 2, 3, 4, 5])) # 5
print(array_sum([1, 2, 3, 4, 5])) # 15
print(array_mean([1, 2, 3, 4, 5])) # 1.9375
print(array_max([1, 12, 3, 4, 5])) # 12