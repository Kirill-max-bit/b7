# Перебираем все четырехзначные числа
for number in range(1000, 10000):
    if number % 133 == 125 and number % 134 == 111:
        print(number)
