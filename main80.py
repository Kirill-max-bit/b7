def queue_time_and_min_service(n, t):
    c = [sum(t[:i+1]) for i in range(n)]
    min_service_index = t.index(min(t)) + 1
    return c, min_service_index


n = 4
t = [5, 3, 8, 2]
c, min_index = queue_time_and_min_service(n, t)
print(f"Время пребывания в очереди: {c}")
print(f"Номер покупателя с минимальным временем обслуживания: {min_index}")
