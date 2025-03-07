# Ввод данных
m = int(input("Введите натуральное число m: "))  # Количество чисел
numbers = []  # Список для хранения чисел

# Ввод чисел d1, d2, ..., dm
for i in range(m):
    num = int(input(f"Введите число d{i + 1}: "))
    numbers.append(num)

# Подсчет количества положительных чисел
count_positive = sum(1 for num in numbers if num > 0)

# Проверка, кратно ли количество трем
is_count_multiple_of_3 = count_positive % 3 == 0

# Вывод результата
print(f"Количество положительных чисел кратно трем: {is_count_multiple_of_3}")
