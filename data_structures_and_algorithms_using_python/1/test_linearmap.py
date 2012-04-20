#!/usr/bin/env python

import unittest

import linearmap

class Test(unittest.TestCase):

    def test_init(self):
        self.m = linearmap.Map()
        self.assertEquals(len(self.m), 0)
        self.assertFalse(1 in self.m)

    def test_add(self):
        self.test_init()
        self.assert_(self.m.add('a',1))
        self.assertFalse(self.m.add('a',1))
        self.assert_('a' in self.m)
        self.assertEquals(len(self.m), 1)

    def test_remove(self):
        self.test_add()
        self.m.remove('a')
        self.assertEquals(len(self.m), 0)
        self.assertFalse(1 in self.m)

if __name__ == "__main__":
    unittest.main()
