class Number(object):
    def __init__(self, n):
        self._base = n
        self._factor = 1

    def __lt__(self, other):
        if self.count() == other.count():
            return self._base < other._base
        return self.count() < other.count()

    def count(self):
        return self._base * self._factor

    def _check(self):
        a = self._factor
        while a % 5 == 0:
            a /= 5
        while a % 3 == 0:
            a /= 3
        while a % 2 == 0:
            a /= 2
        if a != 1:
            return False
        return True

    def next(self):
        self._factor += 1
        while not self._check():
            self._factor += 1


class TestHamming(object):
    def __init__(self):
        self._two = Number(2)
        self._three = Number(3)
        self._five = Number(5)
        self.current = 1

    def get_number(self, n):
        for _ in range(n - 1):
            res = self.get_min()
            while res.count() <= self.current:
                res.next()
                res = self.get_min()
            self.current = res.count()
            res.next()
        return self.current

    def get_min(self):
        return min(self._two, self._three, self._five)