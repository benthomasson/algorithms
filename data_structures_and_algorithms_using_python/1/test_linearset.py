#!/usr/bin/env python

import unittest

import linearset

class Test(unittest.TestCase):

    def test_init(self):
        self.s = linearset.Set()
        self.assertEquals(len(self.s),0)
        self.assertFalse(1 in self.s)

    def test_add(self):
        self.test_init()
        self.s.add(1)
        self.assert_(1 in self.s)

    def test_remove(self):
        self.test_add()
        self.s.remove(1)
        self.assertFalse(1 in self.s)

    def test_eq(self):
        self.test_add()
        self.assert_(self.s == self.s)

    def test_iter(self):
        self.test_add()
        i = iter(self.s)
        self.assertEquals(next(i),1)

    def test_union(self):
        self.test_add()
        self.s2 = linearset.Set()
        self.s2.add(2)
        u = self.s.union(self.s2)
        self.assert_(u != self.s)
        self.assert_(u != self.s2)
        self.assert_(1 in u)
        self.assert_(2 in u)
        self.assertFalse(3 in u)

if __name__ == "__main__":
    unittest.main()
