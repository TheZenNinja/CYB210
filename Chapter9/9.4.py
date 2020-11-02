def sumList(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sumList(list[1:])

newList = [1,2,3,4,5]

print(sumList(newList))