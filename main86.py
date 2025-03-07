def is_sum_greater_than(numbers, threshold=100.78):
    return sum(numbers) > threshold


numbers = [20.5, 30.3, 50.2]
result = is_sum_greater_than(numbers)
print(f"Сумма превышает 100.78: {result}")
