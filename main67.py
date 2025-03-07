def max_sum_pairs(pairs):
    max_sum = max(a + b for a, b in pairs)
    return max_sum


pairs = [(3, 5), (7, 2), (4, 6), (1, 8)]
result = max_sum_pairs(pairs)
print(f"Максимальная сумма значений чисел в паре: {result}")
