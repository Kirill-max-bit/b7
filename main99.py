# Ввод данных
n = int(input("Введите натуральное число n: "))  # Количество чисел
numbers = []  # Список для хранения чисел

# Ввод чисел a1, a2, ..., an
for i in range(n):
    num = int(input(f"Введите число a{i + 1}: "))
    numbers.append(num)

# Ввод пороговых значений m и q
m = int(input("Введите число m: "))
q = int(input("Введите число q: "))

# Вычисление суммы чисел, которые не превышают m
sum_less_than_or_equal_m = sum(num for num in numbers if num <= m)

# Проверка условия
is_sum_greater_than_q = sum_less_than_or_equal_m > q

# Вывод результата
print(f"Сумма чисел, не превышающих {m}, больше {q}: {is_sum_greater_than_q}")
