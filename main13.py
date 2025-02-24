def get_divisors(n):
    """Возвращает отсортированный список всех делителей натурального числа n."""
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors)


# а) Получить все делители
def task_a(n):
    return get_divisors(n)

# б) Найти сумму делителей
def task_b(n):
    return sum(get_divisors(n))

# в) Найти сумму четных делителей
def task_c(n):
    return sum(x for x in get_divisors(n) if x % 2 == 0)

# г) Определить количество делителей
def task_d(n):
    return len(get_divisors(n))

# д) Определить количество нечетных делителей
def task_e(n):
    return len([x for x in get_divisors(n) if x % 2 != 0])

# е) Количество всех делителей и количество четных
def task_f(n):
    divisors = get_divisors(n)
    total = len(divisors)
    even = len([x for x in divisors if x % 2 == 0])
    return total, even

# ж) Найти количество делителей, больших d
def task_g(n, d):
    return len([x for x in get_divisors(n) if x > d])


n = 6
print("а) Делители:", task_a(n))         # [1, 2, 3, 6]
print("б) Сумма делителей:", task_b(n))  # 12
print("в) Сумма четных делителей:", task_c(n))  # 8
print("г) Количество делителей:", task_d(n))    # 4
print("д) Нечетных делителей:", task_e(n))      # 2
print("е) Всего и четных:", task_f(n))          # (4, 2)
print("ж) Делителей > 3:", task_g(n, 3))        # 1

