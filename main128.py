def is_perfect_number(n):
    if n <= 1:
        return False

    divisors = [1] + [i for i in range(2, int(n**0.5) + 1) if n % i == 0]
    [n // i for i in range(2, int(n**0.5) + 1) if n % i == 0 and i != n // i]
    return sum(divisors) == n


n = 28
print(is_perfect_number(n))
