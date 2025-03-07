def best_skier(times):
    min_time = min(times)
    return times.index(min_time) + 1


times = [120, 110, 115, 110, 130]
skier = best_skier(times)
print(f"Лыжник с лучшим результатом стартовал под номером: {skier}")
