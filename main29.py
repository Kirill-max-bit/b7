# Ввод оценок и преобразование в список целых чисел
grades = list(map(int, input("введите число: ").split()))

# Подсчет количества пятерок и двоек
count_5 = grades.count(5)
count_2 = grades.count(2)

# Вывод результатов
print(count_5)
print(count_2)
