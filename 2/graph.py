#!/usr/bin/env python


a, b, c, d, e, f, g, h = range(8)
N = [
    {b, c, d, e ,f},
    {c, e},
    {d},
    {e},
    {f},
    {c, g, h},
    {f, h},
    {f, g},
]

print 1, N
print 2, b in N[a]
print 3, len(N[f])


a, b, c, d, e, f, g, h = range(8)
N = [
    [b, c, d, e ,f],
    [c, e],
    [d],
    [e],
    [f],
    [c, g, h],
    [f, h],
    [f, g],
]

print 4, N
print 5, b in N[a]
print 6, len(N[f])



a, b, c, d, e, f, g, h = range(8)
N = [
    {b:2, c:1, d:3, e:9 ,f:4},
    {c:4, e:3},
    {d:8},
    {e:7},
    {f:5},
    {c:2, g:2, h:2},
    {f:1, h:6},
    {f:9, g:8},
]

print 7, N
print 8, b in N[a]
print 9, len(N[f])


N = {
    'a': set('bcdef'),
    'b': set('ce'),
    'c': set('d'),
    'd': set('e'),
    'e': set('f'),
    'f': set('cgh'),
    'g': set('fh'),
    'h': set('fg'),
}

print 10, N
print 11, 'b' in N['a']
print 12, len(N['f'])

a, b, c, d, e, f, g, h = range(8)

N = [[0,1,1,1,1,1,0,0],
     [0,0,1,0,1,0,0,0],
     [0,0,0,1,0,0,0,0],
     [0,0,0,0,1,0,0,0],
     [0,0,0,0,0,1,0,0],
     [0,0,1,0,0,0,1,1],
     [0,0,0,0,0,1,0,1],
     [0,0,0,0,0,1,1,0]]

print 13, N[a][b]
print 14, sum(N[f])




a, b, c, d, e, f, g, h = range(8)
_ = float('inf')

W = [[0,2,1,3,9,4,_,_],
     [_,0,4,_,3,_,_,_],
     [_,_,0,8,_,_,_,_],
     [_,_,_,0,7,_,_,_],
     [_,_,_,_,0,5,_,_],
     [_,_,2,_,_,0,2,2],
     [_,_,_,_,_,1,0,6],
     [_,_,_,_,_,9,8,0]]

print 15, W[a][b] < _
print 16, sum(1 for w in W[a] if w < _) - 1



