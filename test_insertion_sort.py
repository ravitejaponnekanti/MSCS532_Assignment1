"""Run with: python -m unittest -v."""

import random
import unittest

from insertion_sort import insertion_sort_descending


class InsertionSortTests(unittest.TestCase):
    def test_edge_cases(self):
        cases = [[], [7], [3, 3, 3], [1, 2, 3, 4], [4, 3, 2, 1],
                 [0, -5, 2, -1, 2], [5, 2, 4, 6, 1, 3, 2]]
        for values in cases:
            with self.subTest(values=values):
                expected = sorted(values, reverse=True)
                result = insertion_sort_descending(values)
                self.assertIs(result, values)
                self.assertEqual(result, expected)

    def test_random_lists(self):
        rng = random.Random(532)
        for length in range(100):
            values = [rng.randint(-50, 50) for _ in range(length)]
            expected = sorted(values, reverse=True)
            self.assertEqual(insertion_sort_descending(values), expected)


if __name__ == "__main__":
    unittest.main()
