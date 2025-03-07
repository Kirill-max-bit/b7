# Ввод данных
m = int(input("Введите натуральное число m: "))  # Количество чисел
numbers = []  # Список для хранения чисел

# Ввод чисел a1, a2, ..., am
for i in range(m):
    num = int(input(f"Введите число a{i + 1}: "))
    numbers.append(num)

# Ввод числа p
p = int(input("Введите число p: "))

# Подсчет количества чисел, больших m
count_greater_than_m = sum(1 for num in numbers if num > m)

# Проверка, кратно ли количество p
is_count_multiple_of_p = count_greater_than_m % p == 0

# Вывод результата
print(f"Количество чисел, больших {m}, кратно {p}: {is_count_multiple_of_p}")
