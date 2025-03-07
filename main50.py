def find_last_above_100(numbers):
    # Проходим список с конца
    for i in range(len(numbers) - 1, -1, -1):
        if numbers[i] > 100:
            return i
    return -1  # Если таких чисел нет (хотя по условию они есть)


numbers = [50, 120, 80, 150, 90, 200]
last_index = find_last_above_100(numbers)
print(f"Номер последнего числа, большего 100: {last_index}")
