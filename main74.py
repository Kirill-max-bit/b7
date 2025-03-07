def count_max_elements(sequence):
    max_element = max(sequence)
    return sequence.count(max_element)


sequence = [3, 5, 8, 8, 4]
result = count_max_elements(sequence)
print(f"Количество максимальных элементов: {result}")
