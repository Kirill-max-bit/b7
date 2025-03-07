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
