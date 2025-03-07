def count_min_temperature_days(temperatures):
    min_temp = min(temperatures)
    return temperatures.count(min_temp)


temperatures = [10, 5, 5, 8, 5]
result = count_min_temperature_days(temperatures)
print(f"Количество дней с самой низкой температурой: {result}")
