def max_even_segment(sequence):
    max_len = 0
    current_len = 0
    for num in sequence:
        if num % 2 == 0:
            current_len += 1
            max_len = max(max_len, current_len)
        else:
            current_len = 0
    return max_len


sequence = [2, 4, 6, 1, 2, 8, 10, 3]
result = max_even_segment(sequence)
print(f"Наибольшая длина отрезка из четных чисел: {result}")
