keyList = list(set(['a', 'b']))
keyDict = dict(zip(keyList, [[]for i in keyList]))
keyDict['a'].append(1)
keyDict['a'].append(2)
keyDict['a'].append(3)
keyDict['b'].append(4)

print(keyDict['a'])
print(keyDict['b'])
