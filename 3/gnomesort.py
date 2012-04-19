#!/usr/bin/env python

from random import shuffle

def random_range(length):
    l = range(length)
    shuffle(l)
    print l
    return l

loops = 0
def gnomesort(seq):
    global loops
    i = 0
    while i < len(seq):
        loops += 1
        print 'i:', i
        if i == 0 or seq[i-1] < seq[i]:
            i += 1
        else:
            print 'swap'
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i -= 1
    return seq


#gnomesort(range(10))
loops = 0
#gnomesort(random_range(10))
print loops
r = range(9,0,-1)
print r
gnomesort(r)
print loops
