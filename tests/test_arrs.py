import unittest
from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3, 4], 2, "test") == 3
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([]) == []
    assert arrs.my_slice([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4]
    assert arrs.my_slice([1, 2, 3, 4, 5], 2, 8) == [3, 4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5], 2, 10) == [3, 4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5], 0, 2) == [1, 2]

