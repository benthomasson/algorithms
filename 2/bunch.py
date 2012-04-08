#!/usr/bin/env python

class Bunch(dict):

    def __init__(self, *args, **kwargs):
        super(Bunch, self).__init__(*args, **kwargs)
        self.__dict__ = self

x = Bunch(name="Jayne Cobb", position="Public Relations")
print 1, x.name

T = Bunch
t = T(left=T(left='a', right='b'), right=T(left='c'))
print 2, t.left
print 3, t.left.right
print 4, t['left']['right']
print 5, 'left' in t.right
print 6, 'right' in t.right
