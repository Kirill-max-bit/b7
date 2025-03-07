def average_above_n(x, a, n):
    numbers_above_n = [ai for ai in a if ai > n]
    if not numbers_above_n:
        return None
    return sum(numbers_above_n) / len(numbers_above_n)


x = 5
a = [10, 20, 30, 40, 50]
n = 25
result = average_above_n(x, a, n)
print(result)
