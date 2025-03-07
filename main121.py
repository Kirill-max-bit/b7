def first_max_or_min(n, x):
    max_val = max(x)
    min_val = min(x)
    max_index = x.index(max_val)
    min_index = x.index(min_val)
    if max_index < min_index:
        return "Максимальное"
    else:
        return "Минимальное"


n = 5
x = [3, 1, 4, 1, 5]
result = first_max_or_min(n, x)
print(result)  # Вывод: Минимальное
