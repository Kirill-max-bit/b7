def count_repeated_and_unique(sequence):
    from itertools import groupby
    # Количество повторяющихся чисел
    repeated_count = sum(len(list(g)) - 1 for _, g in groupby(sequence) if
                         len(list(g)) > 1)
    # Количество уникальных чисел
    unique_count = len(set(sequence))
    return repeated_count, unique_count


sequence = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5]
repeated, unique = count_repeated_and_unique(sequence)
print(f"Повторяющихся чисел: {repeated}, Уникальных чисел: {unique}")
