def best_decathlete(athlete1, athlete2):
    total1 = sum(athlete1)
    total2 = sum(athlete2)
    if total1 > total2:
        return "Спортсмен 1"
    elif total2 > total1:
        return "Спортсмен 2"
    else:
        return "Ничья"


athlete1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
athlete2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
result = best_decathlete(athlete1, athlete2)
print(f"Лучший результат: {result}")
