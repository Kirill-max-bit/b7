def best_runners(results):
    sorted_results = sorted(results)
    return sorted_results[:4]


results = [103, 105, 102, 107, 101, 104]
best_team = best_runners(results)
print(f"Четверка лучших бегунов: {best_team}")
