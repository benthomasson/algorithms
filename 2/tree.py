#!/usr/bin/env python


T = [["a","b"], ["c"], ["d", ["e","f"]]]
print 1, T[0][1]
print 2, T[2][1][0]


class Tree:
    def __init__(self, left, right):
        self.left = left
        self.right = right


t = Tree(Tree("a","b"), Tree("c","d"))
print 3, t.right.left
