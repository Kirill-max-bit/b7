def is_prime(n):
    if n <= 1:
        return False
    # Используем генератор списка для проверки делителей
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))


n = 29
print(is_prime(n))
