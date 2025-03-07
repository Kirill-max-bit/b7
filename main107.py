# Ввод данных
n = int(input("Введите натуральное число n: "))  # Количество чисел
numbers = []  # Список для хранения чисел

# Ввод чисел a1, a2, ..., an
for i in range(n):
    num = int(input(f"Введите число a{i + 1}: "))
    numbers.append(num)

# Ввод числа x
x = int(input("Введите число x: "))

# Подсчет количества отрицательных чисел
count_negative = sum(1 for num in numbers if num < 0)

# Проверка условия
is_count_greater_than_x = count_negative > x

# Вывод результата
print(f"Количество отрицательных чисел превышает {x}: {is_count_greater_than_x}")
