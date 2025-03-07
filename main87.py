def is_sum_less_than(numbers, p):
    return sum(numbers) < p


numbers = [10, 20, 30]
p = 70
result = is_sum_less_than(numbers, p)
print(f"Сумма меньше {p}: {result}")
