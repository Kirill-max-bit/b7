def average_even_numbers(c):
    even_numbers = [ci for ci in c if ci % 2 == 0]
    if not even_numbers:
        return None
    return sum(even_numbers) / len(even_numbers)


c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
result = average_even_numbers(c)
print(result)  # Вывод: 7.0
