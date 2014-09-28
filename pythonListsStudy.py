#!/usr/bin/env python

import sys

# empty list
L = []
assert(len(L) == 0)

# mixed types in list
L = [123, 'blah', (1,2,3)]
assert(L[1] == 'blah')

# convert other types into list
L = list('SPAM')
assert(L[1] == 'P')
L = list(range(-4, 4))
assert(L[3] == -1)
assert(L[4:7] == [0, 1, 2])

# concatenate lists
L = [1,2,3] + [4,5,6]
assert(L == [1,2,3,4,5,6])

# contains check
assert(1 in L)
assert(8 not in L)

# append
L = [1,2,3]
L.append(4)
assert(L == [1,2,3,4])

# search for instances in a list
L.append(1)
assert(L.count(1) == 2)

# sorting
L.sort()
assert(L == [1,1,2,3,4])
L = [3,4,2,6,2,7,8]
L.sort(reverse=True)
assert(L == [8,7,6,4,3,2,2])
# string method
L = ['abc', 'BCD', 'aBd']
L.sort()
assert(L == ['BCD','aBd','abc'])
L.sort(key=str.lower)
assert(L == ['abc','aBd','BCD'])
# built-in function
L = ['abc', 'BCD', 'aBd']
L = sorted(L)
assert(L == ['BCD','aBd','abc'])
L = sorted(L,key=str.lower)
assert(L == ['abc','aBd','BCD'])

# reversing
L = [8,7,6,4,3,2,2]
L.reverse()
assert(L == [2,2,3,4,6,7,8])

# removal
L = [4,3,2,1,1]
assert(L.pop(0) == 4) # by index
assert(L == [3,2,1,1])
L.remove(2) # by instance
assert(L == [3,1,1])

# slicing
L = [1,2,3,4,5]
assert(L[1:4] == [2,3,4])
L[1:4] = ['b','l','a','h'] # one more than the elements it replaces
assert(L == [1,'b','l','a','h',5])
L[1:5] = [] # deletion - insert nothing
assert(L == [1,5])
L[1:1] = [10,11] # insertion - delete nothing
assert(L == [1,10,11,5])
L[:0] = [-1,0] # prepend
assert(L == [-1,0,1,10,11,5])

# comprehension
L = [num * 2 for num in range(4,10)]
assert(L == [8,10,12,14,16,18])

# repetition
L = [1,2,3]
L = L * 2
assert(L == [1,2,3,1,2,3])

# append
L = [1,2,3]
L.append(4) # one item
assert(L == [1,2,3,4])
L.extend([5,6,7])
assert(L == [1,2,3,4,5,6,7])

# stack operations
L = [1,2,3]
assert(L.pop() == 3)
assert(L == [1,2])
L.append(4)
assert(L == [1,2,4])

# find the index of an item
assert(L.index(2) == 1)

# deletion
L = [1,2,3,4,5]
del L[1:4]
assert(L == [1,5])

# copying
L = [1,2,3]
LsliceCopy = L[:]
assert(L == LsliceCopy)
assert(L is not LsliceCopy)
LmethodCopy = L.copy()
assert(L == LmethodCopy)
assert(L is not LmethodCopy)
LbuiltinCopy = list(L)
assert(L == LbuiltinCopy)
assert(L is not LbuiltinCopy)

