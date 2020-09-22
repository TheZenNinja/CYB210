def makeDictionary(keys, values):
    dictionary = {}
    for key in keys:
        dictionary[key] = values[keys.index(key)]
    return dictionary

names=['joe','tom','barb','sue','sally']
scores=[10,23,13,18,12]

scoreDict = makeDictionary(names,scores)

print(scoreDict)