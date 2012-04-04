#!/usr/bin/env python
nums = []
nums.append(1)
nums.insert(0, 2)

print nums

seq = range(10)
s = 0
for x in seq:
    s += x

print s

squares = [x ** 2 for x in seq]

print squares

s = 0
for x in seq:
    for y in seq:
        s += x * y

print s
