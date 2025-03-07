def find_max_apartment(people):
    max_people = max(people)
    last_index = len(people) - 1 - people[::-1].index(max_people)
    return last_index + 1
