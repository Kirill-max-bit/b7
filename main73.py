def two_max_elements(sequence):
    sorted_seq = sorted(sequence, reverse=True)
    return sorted_seq[:2]


sequence = [3, 5, 1, 8, 4]
result = two_max_elements(sequence)
print(f"Два максимальных элемента: {result}")
