# Пример данных
numbers = [5, 15, 20, 10, 25, 30, 35, 40, 45]

# Фильтрация чисел больше 10
filtered_numbers = [num for num in numbers if num > 10]

# Вычисление среднего арифметического
average = sum(filtered_numbers) / len(filtered_numbers) if filtered_numbers else 0
print(f"Среднее арифметическое чисел больше 10: {average}")
