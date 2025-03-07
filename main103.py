# Пример данных
numbers = [10, -5, 20, -10, 30, -15, 40, -20, 50, -25]

# Подсчет положительных чисел
positive_count = sum(1 for num in numbers if num > 0)
is_positive_count_less_than_5 = positive_count <= 5
print(f"Количество положительных чисел не превышает 5: {is_positive_count_less_than_5}")
