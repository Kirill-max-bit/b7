def find_farthest_city(distances):
    return max(distances)


distances = [100, 250, 150, 300, 200]
farthest = find_farthest_city(distances)
print(f"Расстояние до самого удаленного города: {farthest} км")
