def is_overload(cargo_weights, capacity):
    return sum(cargo_weights) > capacity


cargo_weights = [100, 200, 300]
capacity = 500
result = is_overload(cargo_weights, capacity)
print(f"Общая масса грузов превышает грузоподъемность: {result}")
