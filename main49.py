def find_last_first_10(numbers):
    # а) Номер последнего числа, равного 10
    last_index = len(numbers) - 1 - numbers[::-1].index(10)

    # б) Номер первого числа, равного 10
    first_index = numbers.index(10)

    return last_index, first_index


numbers = [5, 10, 3, 10, 7, 10, 2]
last_index, first_index = find_last_first_10(numbers)
print(f"Номер последнего числа 10: {last_index}")
print(f"Номер первого числа 10: {first_index}")
