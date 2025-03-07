def is_valid_domino_sequence_a(sequence):
    for i in range(len(sequence) - 1):
        current_right = sequence[i] % 10  # Последняя цифра текущего числа
        next_left = sequence[i + 1] // 10  # Первая цифра следующего числа
        if current_right != next_left:
            return False
    return True


sequence = [12, 23, 34, 45]
print(is_valid_domino_sequence_a(sequence))  


def is_valid_domino_sequence_b(sequence):
    for i in range(len(sequence) - 1):
        current_digits = {sequence[i] // 10, sequence[i] % 10}
        next_digits = {sequence[i + 1] // 10, sequence[i + 1] % 10}
        if not current_digits.intersection(next_digits):
            return False
    return True


sequence = [12, 23, 34, 45]
print(is_valid_domino_sequence_b(sequence))
