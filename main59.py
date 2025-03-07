import math


def largest_square_diagonal(areas):
    max_area = max(areas)
    return math.sqrt(2 * max_area)
