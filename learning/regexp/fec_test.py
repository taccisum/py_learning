import unittest
from fec import *


class FecTest(unittest.TestCase):

    def test_gopt(self):
        args = ['fec.py'] + R'-s @ -o D:\out.txt D:\file.txt'.split(' ')
        opts, args = gopt(args)
        self.assertEqual(2, len(opts))
        self.assertEqual('-s', opts[0][0])
        self.assertEqual('@', opts[0][1])
        self.assertEqual('-o', opts[1][0])
        self.assertEqual(R'D:\out.txt', opts[1][1])
        self.assertEqual(R'D:\file.txt', args[0])


if __name__ == '__main__':
    unittest.main()
