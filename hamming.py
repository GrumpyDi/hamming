class Hamming(object):
    def __init__(self):
        self.curr = 1
        self.number = set([self.curr])

    def get_number(self, n):
        for _ in range(n):
            res = self.get_min()
            self.curr = res
        return self.curr

    def get_min(self):
        self.number |= set([self.curr * 2, self.curr * 3, self.curr * 5])
        res = min(self.number)
        self.number.remove(res)
        return res
