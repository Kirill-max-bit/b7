def max_precipitation_day(precipitations):
    max_precip = max(precipitations)
    last_day = len(precipitations) - 1 - precipitations[::-1].index(max_precip)
    return last_day + 1
