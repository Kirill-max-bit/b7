from collections import defaultdict

# Данные об удалениях
penalties = [(1, 2), (2, 5), (1, 2), (2, 10), (1, 5), (2, 2)]

# Вычисляем статистику
team_stats = defaultdict(lambda: {'count': 0, 'total_time': 0})
for team, duration in penalties:
    team_stats[team]['count'] += 1
    team_stats[team]['total_time'] += duration

# Выводим результаты
for team, stats in team_stats.items():
    print(
        f"Команда {team}: "
        f"Удалений: {stats['count']}, "
        f"Время: {stats['total_time']} мин"
    )
