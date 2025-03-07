def is_win_before_loss(times):
    win_index = times.index(min(times))
    loss_index = times.index(max(times))
    return win_index < loss_index


times = [120, 110, 130, 100, 140]
result = is_win_before_loss(times)
print(result)  # Вывод: True
