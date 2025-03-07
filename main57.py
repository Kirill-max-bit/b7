def find_fastest_car(speeds):
    return max(speeds)


speeds = [180, 200, 220, 190, 210]
fastest = find_fastest_car(speeds)
print(f"Максимальная скорость самого быстрого автомобиля: {fastest} км/ч")
