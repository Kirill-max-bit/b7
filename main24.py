# Данные о количестве детей в каждом классе (1-11 классы)
students_per_class = [25, 30, 28, 32, 27, 29, 26, 31, 24, 30, 28]

# Подсчет общего числа детей в нечетных классах (1, 3, 5, ...)
total_students = sum(students_per_class[i] for i in range(0, len(students_per_class), 2))
print("Общее число детей в нечетных классах:", total_students)
