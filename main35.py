# Ввод количества чисел
n = int(input("Введите количество чисел: "))

# Ввод чисел
numbers = []
for i in range(n):
    num = int(input(f"Введите число {i + 1}: "))
    numbers.append(num)

# Инициализация счетчиков
count_equal_pairs = 0          # а) пары равных чисел
count_zero_pairs = 0           # б) пары нулей
count_even_pairs = 0           # в) пары четных чисел
count_ends_with_5_pairs = 0    # г) пары чисел, оканчивающихся на 5

# Подсчет пар
for i in range(n - 1):  # Проходим до предпоследнего элемента
    a1, a2 = numbers[i], numbers[i + 1]  # Текущее и следующее число

    # а) Пара равных чисел
    if a1 == a2:
        count_equal_pairs += 1

    # б) Пара нулей
    if a1 == 0 and a2 == 0:
        count_zero_pairs += 1

    # в) Пара четных чисел
    if a1 % 2 == 0 and a2 % 2 == 0:
        count_even_pairs += 1

    # г) Пара чисел, оканчивающихся на 5
    if abs(a1) % 10 == 5 and abs(a2) % 10 == 5:
        count_ends_with_5_pairs += 1

# Вывод результатов
print(f"а) Количество пар равных чисел: {count_equal_pairs}")
print(f"б) Количество пар нулей: {count_zero_pairs}")
print(f"в) Количество пар четных чисел: {count_even_pairs}")
print(f"г) Количество пар чисел, оканчивающихся на 5: {count_ends_with_5_pairs}")
