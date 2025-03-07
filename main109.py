# Пример данных (оценки ученика)
grades = [4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5]

# Проверка отсутствия троек
has_no_threes = all(grade != 3 for grade in grades)
print(f"Среди оценок нет троек: {has_no_threes}")
