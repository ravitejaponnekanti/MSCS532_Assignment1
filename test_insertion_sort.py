"""Run with: python -m unittest -v."""

import random
import unittest
from unittest.mock import patch
from io import StringIO

from insertion_sort import insertion_sort_descending, main


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

    def test_keyboard_input(self):
        with patch("builtins.input", return_value=" 5 -2 4 6 4 "), \
                patch("sys.stdout", new_callable=StringIO) as output:
            main()
        self.assertIn("Original array: [5, -2, 4, 6, 4]", output.getvalue())
        self.assertIn("Descending order: [6, 5, 4, 4, -2]", output.getvalue())

    def test_invalid_and_blank_input_retry(self):
        with patch("builtins.input", side_effect=["", "3 hello", "1.5", "3 1"]) as read, \
                patch("sys.stdout", new_callable=StringIO) as output:
            main()
        self.assertEqual(read.call_count, 4)
        self.assertIn("Please enter at least one integer.", output.getvalue())
        self.assertEqual(output.getvalue().count("Invalid input."), 2)
        self.assertIn("Descending order: [3, 1]", output.getvalue())


if __name__ == "__main__":
    unittest.main()
