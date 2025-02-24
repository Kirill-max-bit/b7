# Ввод количества чисел
m = int(input("Введите количество чисел: "))

# Инициализация счетчиков
count_multiple_of_3 = 0
count_multiple_of_7 = 0

# Ввод чисел и подсчет
for i in range(m):
    num = int(input(f"Введите число {i + 1}: "))
    if num % 3 == 0:
        count_multiple_of_3 += 1
    if num % 7 == 0:
        count_multiple_of_7 += 1

# Вывод результатов
print(f"Количество чисел, кратных 3: {count_multiple_of_3}")
print(f"Количество чисел, кратных 7: {count_multiple_of_7}")
