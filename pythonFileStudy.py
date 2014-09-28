#!/usr/bin/env python

import sys
import random

fileName = 'sample.txt'
originalFileContents = """this is the first line
second line
a line again"""

# create file
outputFile = open(fileName, 'w')
outputFile.write(originalFileContents)
outputFile.close()

# update file
outputFile = open(fileName, 'a')
outputFile.write('\nthis is an appended line' + str(random.randint(0, 1000000000000)))
outputFile.close()

# check file contents
inputFile = open(fileName)
print(inputFile.read())
#lineNumber = 1
#for line in inputFile :
  #print('line {}: {}'.format(lineNumber, line))
  #lineNumber += 1
