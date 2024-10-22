import data
from data import Point
from math import sqrt
# Write your functions for each part in the space below.

# Part 1
big_list = [[1, 12, 17], [4, 16], [1], [], [8, 9, 10]]
def first_element(nested_list:list[list[int]]) -> list[int]:
    output_list = []
    for n in nested_list:
        if n != []:
            output_list.append(n[0])
    return output_list

print(first_element(big_list))


# Part 2
big_point_list = [Point(4, 2),
                  Point(7, 12),
                  Point(9, 10)]

def x_coordinates(point_list:list[Point]) -> list[float]:
    output_list = []
    for n in point_list:
        output_list.append(n.x)
    return output_list

print(x_coordinates(big_point_list))
# Part 3
part_3_point_list = [Point(4,2),
                     Point(-4, 17),
                     Point(2, -90),
                     Point(-9, -10)]
def are_in_positive_quadrant(point_list:list[Point]) -> list[Point]:
    output_list = []
    for n in point_list:
        if n.x > 0 and n.y > 0:
            output_list.append(n)
    return output_list

print(are_in_positive_quadrant(part_3_point_list))
# Part 4
def distance(point_a:Point, point_b:Point) -> float:
    length = abs(point_a.x - point_b.x)
    height = abs(point_a.y - point_b.y)
    return sqrt((length ** 2) +
                (height ** 2))

print(distance(Point(0,0), Point(4, 3)))
print(distance(Point(0,0), Point(0,0)))
# Part 5
def manhattan_distance(point_a:Point, point_b:Point) -> float:
    length = abs(point_a.x - point_b.x)
    height = abs(point_a.y - point_b.y)
    return float(length + height)

print(manhattan_distance(Point(0,0), Point(4, 3)))
print(manhattan_distance(Point(0,0), Point(0,0)))
# Part 6
def distance_all(points:list[Point]) -> list[float]:
    output_list = []
    for n in points:
        length = abs(n.x - 0.0)
        height = abs(n.y - 0.0)
        output_list.append(sqrt((length ** 2) +
                                (height ** 2)))
    return output_list


print(distance_all([Point(8, 6), Point(4, 3)]))
print(distance_all([Point(-4, -3), Point(8, -6)]))


