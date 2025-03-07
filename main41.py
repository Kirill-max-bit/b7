def count_grades(grades):
    # Словарь для подсчета оценок
    grade_counts = {2: 0, 3: 0, 4: 0, 5: 0}

    for grade in grades:
        if grade in grade_counts:
            grade_counts[grade] += 1

    return grade_counts


# Пример списка оценок
grades = [5, 4, 3, 5, 2, 4, 5, 3, 4, 5, 2, 3]

# Подсчет оценок
result = count_grades(grades)

# Вывод результатов
print(f"Двоек: {result[2]}")
print(f"Троек: {result[3]}")
print(f"Четверок: {result[4]}")
print(f"Пятерок: {result[5]}")
