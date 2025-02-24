# Предположим, что у нас есть список из 20 целых чисел
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Инициализируем переменную для хранения суммы
sum_even = 0

# Проходим по списку с шагом 1
for i in range(len(a)):
    # Проверяем, является ли индекс четным (начиная с 0, поэтому a2 будет под индексом 1)
    if (i + 1) % 2 == 0:
        sum_even += a[i]

# Выводим результат
print("Сумма элементов с четными индексами:", sum_even)

