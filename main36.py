# Ввод количества чисел
n = int(input("Введите количество чисел: "))

# Ввод чисел
numbers = []
for i in range(n):
    num = float(input(f"Введите число {i + 1}: "))
    numbers.append(num)

# Инициализация счетчика
count_greater_than_neighbors = 0

# Подсчет чисел, больших своих соседей
for i in range(1, n - 1):  # Проходим от второго до предпоследнего элемента
    if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
        count_greater_than_neighbors += 1

# Вывод результата
print(f"Количество чисел, больших своих соседей: {count_greater_than_neighbors}")
