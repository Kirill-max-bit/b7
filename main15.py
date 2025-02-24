# Ввод количества чисел n
n = int(input("Введите количество чисел n: "))

# Ввод числа p
p = float(input("Введите число p: "))

# Инициализация списка для хранения вещественных чисел
numbers = []

# Ввод вещественных чисел b1, b2, ..., bn
for i in range(n):
    b = float(input(f"Введите число b{i+1}: "))
    numbers.append(b)

# Инициализация переменной для хранения суммы
sum_greater_than_p = 0

# Перебор всех чисел в списке
for num in numbers:
    if num > p:
        sum_greater_than_p += num

# Вывод результата
print(f"Сумма чисел, больших {p}: {sum_greater_than_p}")
