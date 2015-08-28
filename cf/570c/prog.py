import unittest
from collections import namedtuple

RUN_TEST = True


class BIT():
    def __init__(self, N=100):
        self.N = N + 1
        self._tr = [0] * self.N

    @classmethod
    def lowbit(cls, x):
        return x & (-x)

    def inc(self, idx, amount):
        while idx <= self.N:
            self._tr[idx] += amount
            idx += BIT.lowbit(idx)

    def sum(self, idx):
        result = 0
        while idx > 0:
            result += self._tr[idx]
            idx -= BIT.lowbit(idx)
        return result

    def sum_of_segment(self, left, right):
        assert left >= 1 and left <= right and right <= self.N
        return self.sum(right) - self.sum(left - 1)

    def get_freq(self, idx):
        assert idx > 0 and idx <= self.N
        return self.sum_of_segment(idx, idx)


class Solution():
    def __init__(self, data):
        self.N = data.length
        self._bitree = BIT(self.N + 1)
        for idx, data_item in enumerate(data):
            self.bitree.inc(idx + 1, data_item)
        self._current_result = 0
        self._init_current_result()

    def _init_current_result(self):
        for i in xrange(1, self.N):
            if (self._bitree.get_freq(i) == 1 and
                    self._bitree.get_freq(i + 1) == 1):
                self._current_result += 1

    def get_result_after_changing(self, idx, new_val):
        old_val = self._bitree.get_freq(idx)
        if old_val == new_val:
            return self._current_result
        if new_val == 1:
            # from 0 to 1
            pass # TODO


class BITTest(unittest.TestCase):
    def setUp(self):
        self.bit_instance = BIT()

    def test_lowbit(self):
        res = self.bit_instance.lowbit(8)
        self.assertEqual(res, 8)
        res = self.bit_instance.lowbit(7)
        self.assertEqual(res, 1)
        res = self.bit_instance.lowbit(6)
        self.assertEqual(res, 2)

    def test_inc(self):
        self.bit_instance.inc(7, 3)
        self.assertEqual(self.bit_instance._tr[7], 3)
        self.bit_instance.inc(1, 5)
        self.assertEqual(self.bit_instance._tr[1], 5)
        self.assertEqual(self.bit_instance._tr[2], 5)
        self.assertEqual(self.bit_instance._tr[4], 5)

    def test_sum(self):
        self.bit_instance.inc(1, 3)
        self.bit_instance.inc(2, 4)
        self.assertEqual(self.bit_instance.sum(2), 7)
        self.bit_instance.inc(5, 3)
        self.assertEqual(self.bit_instance.sum(6), 10)
        self.assertEqual(self.bit_instance.sum(4), 7)

    def test_sum_of_segment(self):
        self.bit_instance.inc(1, 3)
        self.bit_instance.inc(3, 4)
        self.bit_instance.inc(5, 9)
        self.assertEqual(self.bit_instance.sum_of_segment(1, 3), 7)
        self.assertEqual(self.bit_instance.sum_of_segment(1, 5), 16)
        self.assertEqual(self.bit_instance.sum_of_segment(5, 5), 9)

    def test_get_freq(self):
        self.bit_instance.inc(4, 4)
        self.bit_instance.inc(2, 5)
        self.assertEqual(self.bit_instance.get_freq(4), 4)
        self.assertEqual(self.bit_instance.get_freq(1), 0)
        self.assertEqual(self.bit_instance.get_freq(2), 5)

if __name__ == '__main__':
    if RUN_TEST:
        unittest.main()
    n, m = map(lambda x: int(x), raw_input().split(' '))
    data = map(lambda x: 1 if x == '.' else 0, raw_input().split(''))
    sol = Solution(data)
    for i in xrange(m):
        idx, new_data_at_idx = raw_input().split(' ')
        idx = int(idx)
        print sol.get_result_after_changing(
            idx=idx,
            to=new_data_at_idx
        )
