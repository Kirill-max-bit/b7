numbers = ["b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9", "b10"]

# а) Сумма чисел больше 20 превышает 100
sum_greater_than_20 = sum(num for num in numbers if num > 20)
is_sum_greater_than_100 = sum_greater_than_20 > 100
print(is_sum_greater_than_100)

# б) Сумма чисел меньше 50 является четным числом
sum_less_than_50 = sum(num for num in numbers if num < 50)
is_sum_even = sum_less_than_50 % 2 == 0
print(is_sum_even)
