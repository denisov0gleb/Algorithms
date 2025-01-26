class BinarySearch:
    def search_iterative(self, array: list, item) -> int:
        low_ind = 0
        high_ind = len(array) - 1
        while low_ind <= high_ind:
            middle = (low_ind + high_ind) // 2
            guess_value = array[middle]

            if guess_value == item:
                return middle
            elif guess_value > item:
                high_ind = middle - 1
            else:
                low_ind = middle + 1
        return None


if __name__ == "__main__":   
    number_array = [1, 2, 4, 5, 6, 7, 8, 9]
    symbol_array = ['a', 'b', 'd', 'e', 'f']
    
    BS = BinarySearch()
    
    print(f"Found {2} in number_array at {BS.search_iterative(number_array, 2)} position")
    print(f"Found {3} in number_array at {BS.search_iterative(number_array, 3)} position")

    print(f"Found {'a'} in symbol_array at {BS.search_iterative(symbol_array, 'a')} position")
    print(f"Found {'c'} in symbol_array at {BS.search_iterative(symbol_array, 'c')} position")