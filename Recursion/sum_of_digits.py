def sum_of_digits(number):
    if number < 10:
        return number
    else:
        return number % 10 + sum_of_digits(number // 10)


print(sum_of_digits(12345)) # 15