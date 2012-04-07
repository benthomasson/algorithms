#!/usr/bin/env python


# O(1)
nums = []
nums.append(1)
nums.insert(0, 2)

print 1, nums

# O(n)
seq = range(10)
s = 0
for x in seq:
    s += x

print 2, s

#O(n)
squares = [x ** 2 for x in seq]

print 3, squares

#O(n^2)
s = 0
for x in seq:
    for y in seq:
        s += x * y

print 4, s

#O(n^3)
s = 0
for x in seq:
    for y in seq:
        s += x * y
    #print 5.1, s
    for z in seq:
        for w in seq:
            s += x - w
            #print 5.2,  s


print 5, s

seq1 = range(10)
seq2 = range(102)

s = 0
for x in seq1:
    for y in seq2:
        s += x * y 

print 6, s


seq1 = [[0,1], [2], [3, 4, 5]]
s = 0
for seq2 in seq1:
    for x in seq2:
        s += x

print 7, s


seq = range(10)
s = 0
n = len(seq)
for i in range(n-1):
    for j in range(i+1, n):
        s += seq[i] * seq[j]
print 8, s

seq = range(3)
n = len(seq)
for i in range(n-1):
    for j in range(i+1, n):
        print 9, i, j
print 9, s


#O(n) if sorted in best case
def sort_w_check(seq):
    n = len(seq)
    for i in range(n-1):
        if seq[i] > seq[i+1]:
            break
    else:
        return
    raise Exception('Not sorted!')

sort_w_check(range(100))
