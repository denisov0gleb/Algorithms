from random import randint, choice

class SimpleAndBinarySearch:
    def __init__(self):
        self.symbol_array = list(map(chr, range(97, 123)))
        self.symbol = choice(self.symbol_array)
        self.number_array = [x for x in range(0, 1_000_000)]
        self.number = choice(self.number_array)

    def simple_search_iterative(self, array: list, search_value) -> int:
        """
        Simple search
        Complexity: always O(n)
        """
        for ind, value in enumerate(array):
            if value == search_value:
                return ind
        return None
    
    def simple_search_iterative_t(self, array: list, search_value) -> list[int, int]:
        counter = 0
        for ind, value in enumerate(array):
            counter += 1
            if value == search_value:
                return ind, counter
        return None, counter


    def binary_search_iterative(self, array: list, search_value) -> int:
        """
        Binary search
        Complexity: always O(log n)
        """
        low_ind = 0
        high_ind = len(array) - 1
        while low_ind <= high_ind:
            middle = (low_ind + high_ind) // 2
            guess_value = array[middle]
            if guess_value == search_value:
                return middle
            elif search_value > guess_value:
                low_ind = middle + 1
            else:
                high_ind = middle - 1

        return None
    
    def binary_search_iterative_t(self, array: list, search_value) -> list[int, int]:
        counter = 0
        low_ind = 0
        high_ind = len(array) - 1
        while low_ind <= high_ind:
            counter += 1
            middle = (low_ind + high_ind) // 2
            guess_value = array[middle]
            if guess_value == search_value:
                return middle, counter
            elif search_value > guess_value:
                low_ind = middle + 1
            else:
                high_ind = middle - 1

        return None, counter


    def binary_search_recursive(self, array: list, search_value, low = None, high = None) -> int:
        """
        Binary search
        Complexity: always O(log n)
        """
        low_ind = low if low != None else 0
        high_ind = high if high != None else len(array) - 1
        if low_ind <= high_ind:
            middle = (low_ind + high_ind) // 2
            guess_value = array[middle]
            if guess_value == search_value:
                return middle
            elif search_value > guess_value:
                return self.binary_search_recursive(array, search_value, low = middle + 1, high = high_ind)
            else:
                return self.binary_search_recursive(array, search_value, low = low_ind, high = middle - 1)
        else:
            return None
        

    def binary_search_recursive_t(self, array: list, search_value, low = None, high = None, c = None) -> int:
        counter = c if c != None else 0
        low_ind = low if low != None else 0
        high_ind = high if high != None else len(array) - 1
        if low_ind <= high_ind:
            counter += 1
            middle = (low_ind + high_ind) // 2
            guess_value = array[middle]
            if guess_value == search_value:
                return middle, counter
            elif search_value > guess_value:
                return self.binary_search_recursive_t(array, search_value, low = middle + 1, high = high_ind, c = counter)
            else:
                return self.binary_search_recursive_t(array, search_value, low = low_ind, high = middle - 1, c = counter)
        else:
            return None, counter


def test_simple_search(S):
    print(f"\tSimple search")
    result, counter = S.simple_search_iterative_t(S.number_array, S.number)
    print(f"Found {S.number} in number_array at {result} position by {counter} actions in {len(S.number_array)} elements")

    result, counter = S.simple_search_iterative_t(S.symbol_array, S.symbol)
    print(f"Found {S.symbol} in symbol_array at {result} position by {counter} actions in {len(S.symbol_array)} elements")
    print()


def test_binary_search(S):
    print(f"\tBinary search iterative:")
    result, counter = S.binary_search_iterative_t(S.number_array, S.number)
    print(f"Found {S.number} in number_array at {result} position by {counter} actions in {len(S.number_array)} elements")
    result, counter = S.binary_search_iterative_t(S.symbol_array, S.symbol)
    print(f"Found {S.symbol} in symbol_array at {result} position by {counter} actions in {len(S.symbol_array)} elements")
    print()

    print(f"\tBinary search recursive:")
    result, counter = S.binary_search_recursive_t(S.number_array, S.number)
    print(f"Found {S.number} in number_array at {result} position by {counter} actions in {len(S.number_array)} elements")
    result, counter = S.binary_search_recursive_t(S.symbol_array, S.symbol)
    print(f"Found {S.symbol} in symbol_array at {result} position by {counter} actions in {len(S.symbol_array)} elements")
    print()


def table_statistic(S):
    _, simple_number_c = S.simple_search_iterative_t(S.number_array, S.number)
    _, binary_it_number_c = S.binary_search_iterative_t(S.number_array, S.number)
    _, binary_rec_number_c = S.binary_search_recursive_t(S.number_array, S.number)

    lens = len(S.number_array)

    print(f"method_name | elements in array | action counter |")
    print("-"*50)
    print(f"simple      | {lens:17} | {simple_number_c:14} |")
    print(f"binary it   | {lens:17} | {binary_it_number_c:14} |")
    print(f"binary rec  | {lens:17} | {binary_rec_number_c:14} |")


if __name__ == "__main__":   
    Search = SimpleAndBinarySearch()
    test_simple_search(Search)
    test_binary_search(Search)

    table_statistic(Search)