import data
import lab4
import unittest
from lab4 import first_element, x_coordinates
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
    def x_coordinates_test(self):
        big_point_list = [Point(4, 2),
                          Point(7, 12),
                          Point(9, 10)]
        self.assertEqual(x_coordinates(big_point_list), [4, 7, 9])


    # Part 3


    # Part 4


    # Part 5


    # Part 6





if __name__ == '__main__':
    unittest.main()
