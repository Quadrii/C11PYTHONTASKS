import unittest
from util import add


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def testAdd(self):
        self.assertEqual(5, add(2, 3))


if __name__ == '__main__':
    unittest.main()
