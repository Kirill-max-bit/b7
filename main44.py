def average_above_n(numbers, n):
    # Фильтруем числа, большие n
    filtered_numbers = [x for x in numbers if x > n]
    # Вычисляем среднее арифметическое
    return sum(filtered_numbers) / len(filtered_numbers)


numbers = [5, 10, 15, 20, 25]
n = 12
result = average_above_n(numbers, n)
print(f"Среднее арифметическое чисел, больших {n}: {result}")
