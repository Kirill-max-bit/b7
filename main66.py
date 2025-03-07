def class_size_diff(classes):
    return max(classes) - min(classes)


classes = [25, 30, 20, 28, 22]
diff = class_size_diff(classes)
print(f"Разница в численности классов: {diff} учеников")

