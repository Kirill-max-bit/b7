def max_avg_speed(distances, times):
    speeds = [distance / time for distance, time in zip(distances, times)]
    max_speed = max(speeds)
    return speeds.index(max_speed) + 1


distances = [100, 200, 150]  # км
times = [2, 4, 3]            # часы
result = max_avg_speed(distances, times)
print(f"Автомобиль с максимальной средней скоростью: №{result}")
