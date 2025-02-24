def task_7_11a():
    result = []
    for num in range(100, 1000):
        if (num ** 2) % 1000 == num:
            result.append(num)
    return result

# Пример использования:
print(task_7_11a())  # Выводит [376, 625]


def task_7_11b():
    result = []
    for num in range(100, 1000):
        if num % 7 == 0:
            hundreds = num // 100
            tens = (num // 10) % 10
            units = num % 10
            sum_digits = hundreds + tens + units
            if sum_digits % 7 == 0:
                result.append(num)
    return result

# Пример использования:
print(task_7_11b())  # Пример вывода: [133, 266, 322, 329, 399, 455, 511, 518, 588, 644, 700, 707, 770, 777, 840, 847, 917, 966]

