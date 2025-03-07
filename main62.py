def find_lowest_team(points):
    min_point = min(points)
    return points.index(min_point) + 1
