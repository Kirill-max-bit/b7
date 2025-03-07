def count_max_after_adding(sequence, A):
    max_element = max(sequence)
    count_before = sequence.count(max_element)
    if A == max_element:
        return count_before + 1
    elif A < max_element:
        return count_before
    else:
        return 1


sequence = [8, 3, 8, 8, 5]
A1, A2 = 0, 8
result1 = count_max_after_adding(sequence, A1)
result2 = count_max_after_adding(sequence, A2)
print(f"При A = 0: {result1}, При A = 8: {result2}")
