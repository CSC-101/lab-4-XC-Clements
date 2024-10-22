import data
import lab4
import unittest
from lab4 import first_element, x_coordinates, are_in_positive_quadrant, manhattan_distance, distance, distance_all
from data import Point

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)


    def test_first_element_2(self):
        big_list = [[1, 12, 17], [4, 16], [1], [], [8, 9, 10]]
        self.assertEqual(first_element(big_list), [1, 4, 1, 8])

    # Part 2
    def test_x_coordinates_1(self):
        big_point_list = [Point(4, 2),
                          Point(7, 12),
                          Point(9, 10)]
        self.assertEqual(x_coordinates(big_point_list), [4, 7, 9])

    def test_x_coordinates_2(self):
        big_point_list = [Point(6, 0),
                          Point(1, 12),
                          Point(10, 4)]
        self.assertEqual(x_coordinates(big_point_list), [6, 1, 10])


    # Part 3
    def test_are_in_positive_quadrant_1(self):
        part_3_point_list = [Point(4, 2),
                             Point(-4, 17),
                             Point(2, -90),
                             Point(-9, -10)]
        self.assertEqual(are_in_positive_quadrant(part_3_point_list), [Point(4,2)])
    def test_are_in_positive_quadrant_2(self):
        part_3_point_list = [Point(4, -2),
                             Point(9, 17),
                             Point(2, -90),
                             Point(-9, -10)]
        self.assertEqual(are_in_positive_quadrant(part_3_point_list), [Point(9,17)])


    # Part 4
    def test_distance_1(self):
        self.assertEqual(distance(Point(0,0), Point(4, 3)), 5.0)
    def test_distance_2(self):
        self.assertEqual(distance(Point(0,0), Point(0,0)), 0.0)

    # Part 5
    def test_manhattan_distance_1(self):
        self.assertEqual(manhattan_distance(Point(0,0), Point(4, 3)), 7.0)

    def test_manhattan_distance_2(self):
        self.assertEqual(manhattan_distance(Point(0,0), Point(0, 0)), 0.0)


    # Part 6
    def test_distance_all_1(self):
        self.assertEqual(distance_all([Point(8, 6), Point(4, 3)]), [10.0, 5.0])

    def test_distance_all_2(self):
        self.assertEqual(distance_all([Point(-4, -3), Point(8, -6)]), [5.0, 10.0])


if __name__ == '__main__':
    unittest.main()
