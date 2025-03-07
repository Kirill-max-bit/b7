def count_valid_triangles(triples):
    count = 0
    for a, b, c in triples:
        if a + b > c:  # Проверка условия треугольника
            count += 1
    return count


# Пример использования
triples = [
    (2, 3, 4),  # Подходит (2 + 3 > 4)
    (1, 2, 3),  # Не подходит (1 + 2 == 3)
    (5, 5, 5),  # Подходит (5 + 5 > 5)
    (4, 5, 10)  # Не подходит (4 + 5 < 10)
]

print(count_valid_triangles(triples))  # Вывод: 2
