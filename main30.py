# Пример списка годов рождения
years_of_birth = [1980, 1992, 1975, 1986, 1995, 1984, 1991, 1987, 1983, 1998]

# Инициализация счетчиков
count_before_1985 = 0
count_after_1990 = 0

# Проход по списку и подсчет
for year in years_of_birth:
    if year < 1985:
        count_before_1985 += 1
    elif year > 1990:
        count_after_1990 += 1

# Вывод результатов
print(f"Число людей, родившихся до 1985 года: {count_before_1985}")
print(f"Число людей, родившихся после 1990 года: {count_after_1990}")
