#!/usr/bin/env python

import sys
import decimal
from decimal import Decimal

decimal.getcontext().prec = 2

twoPlaces = Decimal('0.19')
print(twoPlaces)
twoPlaces += Decimal('.005')
print(twoPlaces)
#print(Decimal.from_float(34.82))

