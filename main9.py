# Перебираем двузначные числа
for number in range(10, 100):
    # Разделяем число на цифры
    digit1 = number // 10  # Первая цифра
    digit2 = number % 10   # Вторая цифра
    # Сумма квадратов цифр
    sum_of_squares = digit1**2 + digit2**2
    # Проверяем, делится ли сумма квадратов на 13
    if sum_of_squares % 13 == 0:
        print(number)
