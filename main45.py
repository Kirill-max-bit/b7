def average_even(numbers):
    # Фильтруем четные числа
    even_numbers = [x for x in numbers if x % 2 == 0]
    # Вычисляем среднее арифметическое
    return sum(even_numbers) / len(even_numbers)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
result = average_even(numbers)
print(f"Среднее арифметическое четных чисел: {result}")
