#!/usr/bin/env python

import sys

# format strings
eater = 'aardvark'
number = 1
eaten = 'ant'
formattedStr = 'Method formatting: {} eats {} {}'.format(eater, number, eaten)
print(formattedStr)
formattedStr = 'Expression formatting: %s eats %d %s' % (eater, number, eaten)
print(formattedStr)

# remove whitepace
withWhitespace = '    blah '
print("withWhitespace='{}'".format(withWhitespace))
withoutWhitespace = withWhitespace.strip()
print("withoutWhitespace='{}'".format(withoutWhitespace))

# digit check
aNumber = '3535'
print("{} is a digit? {}".format(aNumber, aNumber.isdigit())) # true
aNumber = 'bell'
print("{} is a digit? {}".format(aNumber, aNumber.isdigit())) # false
aNumber = 'b55ell'
print("{} is a digit? {}".format(aNumber, aNumber.isdigit())) # false

# string comprehension
print(''.join([c * 2 for c in 'blah']))

# searching within a string
subString = "ABC"
wholeString = "spamABCblah"
print('{} in {}? {}'.format(subString, wholeString, subString in wholeString))

# slicing
someString = 'blah'
print('middle two letters of {} are {}'.format(someString, someString[1:3]))
print('copied version of {} is {}'.format(someString, someString[:]))

# step slicing
embeddedAlphabet = "1a2b3c4d5e6f7g8h9i1j2k3l4m5n6o7p8q9r1s2t3u4v5w6x7y8z"
print('extracted embedded alphabet is {}'.format(embeddedAlphabet[1::2]))
print('extracted embedded alphabet reversed is {}'.format(embeddedAlphabet[::-2]))
print('extracted embedded alphabet reversed in two steps is {}'.format(embeddedAlphabet[1::2][::-1]))
print('extracted embedded alphabet first four letters reversed is {}'.format(embeddedAlphabet[1::2][3::-1]))

# convert number to string and vice versa
print('string form of 42 = {}'.format(str(42)))
print('int form of "42" = {}'.format(int('42')))
print('float form of "42" = {}'.format(float('42')))
print('number code for "S" = {}'.format(ord('S')))
print('character for number code 83 = {}'.format(chr(83)))

# turn a string into a list
S = 'SPAM'
L = list(S)
print('2 character in {} is equal to "P"? {}'.format(S, L[1] == 'P'))
L[1] = 'x'
L[2] = 'x'
print('replaced middle characters with x = {}'.format(''.join(L)))

# formatting with templating characteristics
context = {'name':'Josh Taylor','age':34, 'married':'yes'}
template = '%(name)s is %(age)d years old and his marriage status is %(married)s'
print(template % context)
# using variables as the context
name = 'Josh Taylor'
age = 34
married = 'maybe'
print(template % vars())

