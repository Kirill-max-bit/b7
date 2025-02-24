def task_7_10(n):
    result = []
    for num in range(10, 100):
        tens = num // 10
        units = num % 10
        if num % n == 0 or tens == n or units == n:
            result.append(num)
    return result

# Пример использования:
n = 5
print(task_7_10(n))  # Выводит все двузначные числа, делящиеся на 5 или содержащие цифру 5
