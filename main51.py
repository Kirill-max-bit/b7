def find_last_negative(numbers):
    # Проходим список с конца
    for i in range(len(numbers) - 1, -1, -1):
        if numbers[i] < 0:
            return i
    return -1  # Если таких чисел нет (хотя по условию они есть)


numbers = [5, -3, 7, -2, 10, -1]
last_index = find_last_negative(numbers)
print(f"Номер последнего отрицательного числа: {last_index}")
