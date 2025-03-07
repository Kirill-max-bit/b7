def skating_score(scores):
    if len(scores) < 3:
        return 0.0  # Недостаточно оценок
    copy = list(scores)
    copy.remove(max(copy))
    copy.remove(min(copy))
    return sum(copy) / len(copy)
