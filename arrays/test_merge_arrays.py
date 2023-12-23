import unittest

from merge_arrays import merge_arrays


class TestMergeArrays(unittest.TestCase):
    """Returns a sorted list with no duplicates when given two non-empty arrays"""

    def test_merge_arrays_no_duplicates_sorted(self):
        # Arrange
        array_a = [1, 3, 5]
        array_b = [2, 4, 6]

        # Act
        result = merge_arrays(array_a, array_b)

        # Assert
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])
