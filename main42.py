def count_results(points):
    wins = draws = losses = 0

    for point in points:
        if point == 3:
            wins += 1
        elif point == 1:
            draws += 1
        elif point == 0:
            losses += 1

    return wins, draws, losses


# Пример списка очков за игры
points = [3, 1, 0, 3, 1, 3, 0, 3, 1, 0]

# Подсчет результатов
wins, draws, losses = count_results(points)

# Вывод результатов
print(f"Выигрышей: {wins}")
print(f"Ничьих: {draws}")
print(f"Проигрышей: {losses}")
