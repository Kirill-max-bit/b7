def min_zero_segment(sequence):
    min_len = float('inf')
    current_len = 0
    for num in sequence:
        if num == 0:
            current_len += 1
        else:
            if current_len > 0:
                min_len = min(min_len, current_len)
            current_len = 0
    if current_len > 0:
        min_len = min(min_len, current_len)
    return min_len if min_len != float('inf') else 0


sequence = [0, 1, 0, 0, 0, 1, 0, 0]
result = min_zero_segment(sequence)
print(f"Наименьшая длина отрезка из нулей: {result}")
