def parse_matches(numbers):
    matches = []
    for num in numbers:
        scored = num // 10
        conceded = num % 10
        matches.append((scored, conceded))
    return matches


numbers = [32, 11, 0, 22]
matches = parse_matches(numbers)
print(f"Результаты игр: {matches}")
