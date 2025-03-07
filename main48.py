def average_height(heights):
    # Фильтруем рост мальчиков и девочек
    boys = [h for h in heights if h < 0]
    girls = [h for h in heights if h >= 0]

    # Вычисляем средний рост
    avg_boys = sum(boys) / len(boys)
    avg_girls = sum(girls) / len(girls)

    return avg_boys, avg_girls


heights = [160, -170, 155, -180, 165, -175]
avg_boys, avg_girls = average_height(heights)
print(f"Средний рост мальчиков: {abs(avg_boys)}")
print(f"Средний рост девочек: {avg_girls}")
