# Пример данных: рост учеников (отрицательные числа — мальчики, положительные — девочки)
heights = [160, -170, 155, -180, 165, -175, 150, -185]

# Разделение на мальчиков и девочек
boys = [abs(height) for height in heights if height < 0]  # Берем модуль для мальчиков
girls = [height for height in heights if height > 0]  # Девочки остаются с положительными значениями

# Проверка, есть ли данные для мальчиков и девочек
if not boys or not girls:
    print("Недостаточно данных для сравнения.")
else:
    # Вычисление среднего роста мальчиков
    average_boy_height = sum(boys) / len(boys)

    # Вычисление среднего роста девочек
    average_girl_height = sum(girls) / len(girls)

    # Проверка, превышает ли средний рост мальчиков средний рост девочек более чем на 10 см
    if average_boy_height - average_girl_height > 10:
        print(f"Средний рост мальчиков ({average_boy_height} см) превышает средний рост девочек ({average_girl_height} см) более чем на 10 см.")
    else:
        print(f"Средний рост мальчиков ({average_boy_height} см) НЕ превышает средний рост девочек ({average_girl_height} см) более чем на 10 см.")
