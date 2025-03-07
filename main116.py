def average_multiples_of_n(m, a, n):
    multiples = [ai for ai in a if ai % n == 0]
    if not multiples:
        return None
    return sum(multiples) / len(multiples)


m = 6
a = [10, 15, 20, 25, 30, 35]
n = 5
result = average_multiples_of_n(m, a, n)
print(result)  # Вывод: 20.0
