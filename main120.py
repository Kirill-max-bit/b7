# Пример данных (массы людей)
masses = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140]

# Нахождение максимальной и минимальной массы
max_mass = max(masses)
min_mass = min(masses)

# Проверка условия
is_max_more_than_twice_min = max_mass > 2 * min_mass
print(f"Масса самого тяжелого человека превышает массу самого легкого более чем в 2 раза: {is_max_more_than_twice_min}")
