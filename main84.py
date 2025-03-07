def game_results(matches):
    results = []
    for scored, conceded in matches:
        if scored > conceded:
            results.append("выигрыш")
        elif scored == conceded:
            results.append("ничья")
        else:
            results.append("проигрыш")
    return results


matches = [(3, 2), (1, 1), (0, 2), (2, 2)]
results = game_results(matches)
print(f"Результаты игр: {results}")


def count_wins(matches):
    return sum(1 for scored, conceded in matches if scored > conceded)


matches = [(3, 2), (1, 1), (0, 2), (2, 2)]
wins = count_wins(matches)
print(f"Количество выигрышей: {wins}")


def count_wins_losses(matches):
    wins = sum(1 for scored, conceded in matches if scored > conceded)
    losses = sum(1 for scored, conceded in matches if scored < conceded)
    return wins, losses


matches = [(3, 2), (1, 1), (0, 2), (2, 2)]
wins, losses = count_wins_losses(matches)
print(f"Выигрыши: {wins}, Проигрыши: {losses}")


def count_results(matches):
    wins = sum(1 for scored, conceded in matches if scored > conceded)
    draws = sum(1 for scored, conceded in matches if scored == conceded)
    losses = sum(1 for scored, conceded in matches if scored < conceded)
    return wins, draws, losses


matches = [(3, 2), (1, 1), (0, 2), (2, 2)]
wins, draws, losses = count_results(matches)
print(f"Выигрыши: {wins}, Ничьи: {draws}, Проигрыши: {losses}")


def count_big_wins(matches):
    return sum(1 for scored, conceded in matches if scored - conceded >= 3)


matches = [(3, 2), (1, 1), (0, 2), (4, 0)]
big_wins = count_big_wins(matches)
print(f"Количество игр с разностью мячей >= 3: {big_wins}")


def total_points(matches):
    points = 0
    for scored, conceded in matches:
        if scored > conceded:
            points += 3
        elif scored == conceded:
            points += 1
    return points


matches = [(3, 2), (1, 1), (0, 2), (2, 2)]
points = total_points(matches)
print(f"Общее число очков: {points}")
