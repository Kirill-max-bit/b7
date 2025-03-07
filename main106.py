# Ввод данных
n = int(input("Введите натуральное число n: "))  # Количество чисел
numbers = []  # Список для хранения чисел

# Ввод чисел c1, c2, ..., cn
for i in range(n):
    num = int(input(f"Введите число c{i + 1}: "))
    numbers.append(num)

# Подсчет количества чисел, меньших 20
count_less_than_20 = sum(1 for num in numbers if num < 20)

# Проверка условия
is_count_equal_to_5 = count_less_than_20 == 5

# Вывод результата
print(f"Количество чисел, меньших 20, равно пяти: {is_count_equal_to_5}")
