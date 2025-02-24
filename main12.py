def task_7_12():
    total = 0
    for num in range(31, 100):
        if num % 3 == 0 and num % 10 in {2, 4, 8}:
            total += num
    return total

# Пример использования:
print(task_7_12())  # Выводит 378
