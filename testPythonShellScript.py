#!/usr/bin/env python

import sys

# format strings
eater = 'aardvark'
eaten = 'ant'
formattedStr = '{} eats {}'.format(eater, eaten)
print(formattedStr)

# remove whitepace
withWhitespace = '    blah '
print('withWhitespace: {}'.format(withWhitespace))
withoutWhitespace = withWhitespace.strip()
print('withoutWhitespace: {}'.format(withoutWhitespace))

# something new

