def max_precipitation_day(precipitations):
    max_precip = max(precipitations)
    last_day = len(precipitations) - 1 - precipitations[::-1].index(max_precip)
    return last_day + 1


precipitations = [5, 10, 15, 10, 20, 15]
day = max_precipitation_day(precipitations)
print(f"Самое большое количество осадков выпало {day} числа")
