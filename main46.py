def average_multiple(numbers, n):
    # Фильтруем числа, кратные n
    multiples = [x for x in numbers if x % n == 0]
    # Вычисляем среднее арифметическое
    return sum(multiples) / len(multiples)


numbers = [10, 15, 20, 25, 30]
n = 5
result = average_multiple(numbers, n)
print(f"Среднее арифметическое чисел, кратных {n}: {result}")
