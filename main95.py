# Пример данных
numbers = [1.5, 2.0, 3.5, 4.0, 5.5, 6.0]
s = 1000  # Пример значения s

# Вычисляем произведение
product = 1
for num in numbers:
    product *= num

# Проверяем условие
is_greater_than_s = product > s
print(f"Произведение больше {s}: {is_greater_than_s}")
