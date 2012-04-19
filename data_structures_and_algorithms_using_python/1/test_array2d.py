#!/usr/bin/env python

import unittest

import array2d


class Test(unittest.TestCase):

    def test_init(self):
        self.a = array2d.Array2D(10, 5)
        self.assertEquals(self.a[0,0],None)


if __name__ == "__main__":
    unittest.main()
