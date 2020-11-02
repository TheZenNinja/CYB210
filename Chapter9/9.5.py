def FindMin(list):
    if len(list) == 1:
        return list[0]
    else:
        return min(list[0], FindMin(list[1:]))


numList = [1,2,3,4,5,6]
print(FindMin(numList))

numList = [48,5484,486,486,54,5]
print(FindMin(numList))

numList = [48,5484,2,486,54,5]
print(FindMin(numList))