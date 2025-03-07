from math import prod

# Пример данных
numbers = [5, 10, 15, 20, 25, 30, 35, 40]

# Вычисляем произведение
product = prod(numbers)
is_less_than_10000 = product < 10000
print(f"Произведение меньше 10 000: {is_less_than_10000}")
