# Ввод данных
n = int(input("Введите натуральное число n: "))  # Количество чисел
numbers = []  # Список для хранения чисел

# Ввод чисел d1, d2, ..., dn
for i in range(n):
    num = int(input(f"Введите число d{i + 1}: "))
    numbers.append(num)

# Ввод пороговых значений m и p
m = int(input("Введите число m: "))
p = int(input("Введите число p: "))

# Вычисление суммы чисел, которые не превышают m
sum_less_than_or_equal_m = sum(num for num in numbers if num <= m)

# Проверка, кратна ли сумма числу p
is_sum_multiple_of_p = sum_less_than_or_equal_m % p == 0

# Вывод результата
print(f"Сумма чисел, не превышающих {m}, кратна {p}: {is_sum_multiple_of_p}")
