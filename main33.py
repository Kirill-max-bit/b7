# Пример списка чисел
numbers = [3.5, -2.1, 0, -4.7, 1.2]

# Подсчет положительных и отрицательных чисел
count_positive = sum(1 for num in numbers if num > 0)
count_negative = sum(1 for num in numbers if num < 0)

# Вывод результатов
print(f"Количество положительных чисел: {count_positive}")
print(f"Количество отрицательных чисел: {count_negative}")
