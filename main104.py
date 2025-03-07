# Ввод данных
numbers = []  # Список для хранения чисел

# Ввод 10 вещественных чисел
for i in range(10):
    num = float(input(f"Введите число x{i + 1}: "))
    numbers.append(num)

# Подсчет количества чисел, не превышающих 50.55
count_less_than_or_equal_50_55 = sum(1 for num in numbers if num <= 50.55)

# Проверка, кратно ли количество четырем
is_count_multiple_of_4 = count_less_than_or_equal_50_55 % 4 == 0

# Вывод результата
print(f"Количество чисел, не превышающих 50.55, кратно четырем: {is_count_multiple_of_4}")
