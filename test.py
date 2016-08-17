import unittest
import time
from hamming import Hamming
from test_class import TestHamming


class Joker(object):
    def __init__(self):
        h = Hamming()
        h.get_number(5000)
        self.base = h.base


joker = Joker()


def hamming(n):
    h = Hamming()
    return h.get_number(n)


def test_hamming(n):
    h = TestHamming()
    if n == 1:
        return h.current
    return h.get_number(n)


def greedy_hamming(n):
    return joker.base[n]


class TestStringMethods(unittest.TestCase):
    def test_first_two_hundred(self):
        for i in range(1, 200):
            self.assertEqual(hamming(i), test_hamming(i))

    def test_greedy(self):
        t = time.time()
        for i in range(1, 5000):
            greedy_hamming(i)
        self.assertTrue(time.time() - t < 0.1)


if __name__ == "__main__":
    unittest.main()
