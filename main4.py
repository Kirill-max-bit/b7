a = int(input("Введите a: "))
b = int(input("Введите b: "))

total_sum = 0

for number in range(a, b + 1):
    if number % 4 == 0:
        total_sum += number

print("Сумма чисел, кратных четырем, от", a, "до", b, ":", total_sum)
