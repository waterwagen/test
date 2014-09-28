#!/usr/bin/env python

import sys
from random import randint

numAverages = 10000
randomRangeMinimum = 0
randomRangeMaximum = 10000
avgRandomTotal = 0
for j in range(0,numAverages) :
  maxRandom = randomRangeMinimum - 1
  minRandom = randomRangeMaximum + 1
  totalRandom = 0
  numRandoms = 100
  for i in range(0,numRandoms) :
    randomInt = randint(randomRangeMinimum,randomRangeMaximum)
    maxRandom = max(maxRandom, randomInt)
    minRandom = min(minRandom, randomInt)
    totalRandom += randomInt

  #print('minimum random found is {}'.format(minRandom))
  #print('maximum random found is {}'.format(maxRandom))
  avgRandom = totalRandom / numRandoms
  #print('average random found is {}'.format(avgRandom))
  avgRandomTotal += avgRandom

print('average avgRandom is {}'.format(avgRandomTotal / numAverages))

