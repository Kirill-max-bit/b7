def last_negative_index(k, a):
    for i in range(k - 1, -1, -1):  # Идем с конца списка
        if a[i] < 0:
            return i + 1  # Номера считаем с 1
    return None  # Если отрицательных чисел нет


k = 6
a = [10, -5, 20, -3, 30, -1]
result = last_negative_index(k, a)
print(result)  # Вывод: 6
