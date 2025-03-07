# Пример данных
numbers = [15, 25, 30, 10, 40, 50, 60, 70, 80, 90]

# а) Сумма чисел больше 20 превышает 100
sum_greater_than_20 = sum(num for num in numbers if num > 20)
is_sum_greater_than_100 = sum_greater_than_20 > 100
print(f"Сумма чисел больше 20 превышает 100: {is_sum_greater_than_100}")

# б) Сумма чисел меньше 50 является четным числом
sum_less_than_50 = sum(num for num in numbers if num < 50)
is_sum_even = sum_less_than_50 % 2 == 0
print(f"Сумма чисел меньше 50 четная: {is_sum_even}")
