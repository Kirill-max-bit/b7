def max_sum_neighbors(sequence):
    return max(sequence[i] + sequence[i+1] for i in range(len(sequence) - 1))


sequence = [1, 3, 5, 2, 4]
result = max_sum_neighbors(sequence)
print(f"Максимальная сумма двух соседних чисел: {result}")


def min_sum_neighbors(sequence):
    return min(sequence[i] + sequence[i+1] for i in range(len(sequence) - 1))


sequence = [1, 3, 5, 2, 4]
result = min_sum_neighbors(sequence)
print(f"Минимальная сумма двух соседних чисел: {result}")
