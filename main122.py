def first_oldest_or_youngest(ages):
    oldest = max(ages)
    youngest = min(ages)
    oldest_index = ages.index(oldest)
    youngest_index = ages.index(youngest)
    if oldest_index < youngest_index:
        return "Самый старший"
    else:
        return "Самый молодой"


ages = [25, 30, 20, 35, 20]
result = first_oldest_or_youngest(ages)
print(result)  # Вывод: Самый старший
