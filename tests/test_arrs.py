import unittest
from utils.arrs import get
from utils.arrs import my_slice


class TestFunction(unittest.TestCase):

    def test_get(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(get(array, 2), 3)
        self.assertIsNone(get(array, 10), "default")

    def test_slice(self):
        self.assertEqual(my_slice([]), [])
        self.assertEqual(my_slice([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(my_slice([1, 2, 3, 4, 5], 1, 4), [2, 3, 4])
        self.assertEqual(my_slice([1, 2, 3, 4, 5], 2, 8), [3, 4, 5])
        self.assertEqual(my_slice([1, 2, 3, 4, 5], 2, 10), [3, 4, 5])


if __name__ == '__main__':
    unittest.main()


