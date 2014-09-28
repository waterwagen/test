#!/usr/bin/env python

import sys

key1 = 'red'
value1 = 'booyah'
key2 = 'blue'
value2 = 'heyho'
key3 = 'orange'
value3 = 'ohhhh yeeeeeah'
keyValuePairs = [(key1, value1), (key2, value2), (key3, value3)]
testMap = {} # empty map literal
for pair in keyValuePairs :
  testMap[pair[0]] = pair[1]
#testMap[key1] = value1
#testMap[key2] = value2

print(testMap)
testMap[key1] = 3
print(testMap)

keys = list(testMap.keys())
keys.sort()
print(keys)

testMap = {'age':22, 'name':{'firstName':'Bob', 'lastName':'Jones'}} # map literal with nested map
assert(testMap['age'] == 22)
assert(testMap['name'] == {'firstName':'Bob','lastName':'Jones'})

testMap = dict(name='Jimmy', age=40) # another map building approach
print(testMap)
assert('age' in testMap)
assert('name' in testMap)
assert('blah' not in testMap)

entries = testMap.items() # key-value entries (as tuples)
assert({entry[0] for entry in entries} == {'age', 'name'})
print(entries)

del testMap['age']
assert({entry[0] for entry in entries} == {'name'})

assert('blah' not in testMap)
assert(testMap.get('blah','N/A') == 'N/A')

# merging two maps, clashes are overwritten without warning
testMap['age'] = 22
assert('age' in testMap)
testMap2 = {'age':45,'color':'red'}
testMap.update(testMap2)
assert(testMap == {'name':'Jimmy', 'age':45, 'color':'red'})

# copying a map
testMap2 = testMap.copy()
assert(testMap is not testMap2)
assert(testMap == testMap2)
