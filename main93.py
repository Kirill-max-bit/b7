def cheaper_set(set1, set2):
    total1 = sum(set1)
    total2 = sum(set2)
    if total1 < total2:
        return "Набор 1"
    elif total2 < total1:
        return "Набор 2"
    else:
        return "Стоимость одинакова"


set1 = [100, 200, 300]
set2 = [150, 250, 350]
result = cheaper_set(set1, set2)
print(f"Более дешевый набор: {result}")
