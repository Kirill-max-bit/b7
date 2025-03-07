def count_max_elements(sequence):
    max_element = max(sequence)
    return sequence.count(max_element)


sequence = [3, 5, 8, 8, 4]
result = count_max_elements(sequence)
print(f"Количество максимальных элементов: {result}")


def count_min_elements(sequence):
    min_element = min(sequence)
    return sequence.count(min_element)


sequence = [3, 5, 1, 1, 4]
result = count_min_elements(sequence)
print(f"Количество минимальных элементов: {result}")
