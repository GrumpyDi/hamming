import unittest
from hamming import Hamming
from test_class import TestHamming


def hamming(n):
    h = Hamming()
    return h.get_number(n)


def test_hamming(n):
    h = TestHamming()
    if n == 1:
        return h.current
    return h.get_number(n)


class TestStringMethods(unittest.TestCase):
    def test_first_two_hundred(self):
        for i in range(1, 200):
            self.assertEqual(hamming(i), test_hamming(i))


if __name__ == "__main__":
    unittest.main()
