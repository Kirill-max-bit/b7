def max_density(masses, volumes):
    densities = [mass / volume for mass, volume in zip(masses, volumes)]
    return max(densities)


masses = [10, 20, 15]  # кг
volumes = [5, 10, 3]   # см³
result = max_density(masses, volumes)
print(f"Максимальная плотность материала: {result:.2f} кг/см³")
