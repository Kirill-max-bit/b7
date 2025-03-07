def track_best_result(results):
    best_result = float('inf')  # Инициализация лучшего результата

    for result in results:
        if result < best_result:
            best_result = result
        print(f"Лучший результат после ввода {result}: {best_result}")


results = [120, 115, 110, 125, 105]
track_best_result(results)
