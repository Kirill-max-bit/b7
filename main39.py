import math


def calculate_hit_percentage(data, R, H, P, g=9.8):
    hit_count = 0
    total = len(data)

    for alpha, v0 in data:
        # Переводим угол из градусов в радианы
        alpha_rad = math.radians(alpha)

        # Время, когда снаряд достигнет расстояния R
        t = R / (v0 * math.cos(alpha_rad))

        # Высота снаряда в момент времени t
        y = v0 * t * math.sin(alpha_rad) - (g * t**2) / 2

        # Проверка попадания в цель
        if H <= y <= H + P:
            hit_count += 1

    # Вычисление процента попаданий
    if total == 0:
        return 0
    return (hit_count / total) * 100


data = [
    (45, 100),  # Угол 45 градусов, начальная скорость 100 м/с
    (30, 150),  # Угол 30 градусов, начальная скорость 150 м/с
    (60, 80),   # Угол 60 градусов, начальная скорость 80 м/с
]

R = 1000  # Расстояние до цели (м)
H = 10    # Высота основания цели (м)
P = 5     # Высота цели (м)

hit_percentage = calculate_hit_percentage(data, R, H, P)
print(f"Процент попаданий: {hit_percentage:.2f}%")
