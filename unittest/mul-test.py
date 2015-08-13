import unittest as T
from mul import multiply


class TestMul(T.TestCase):
    def setUp(self):
        pass

    def test_3_mul_4(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_a_mul_3(self):
        self.assertEqual(multiply('a', 3), 'aaa')

if __name__ == '__main__':
    T.main()
