import random;

def CreateTempConvTable(listF):
    tableFile = open("tempconv.txt", "w")

    tableFile.write("%10s, %10s\n" % ("Fahrenheit", "Celsius,"))
    for i in range(len(listF)):
        tableFile.write("%10.3f, %10.3f,\n" % (listF[i], (listF[i]-32) * 5 / 9))
    tableFile.close()
    print("complete")

tempF = []

for i in range(20):
    tempF.append(random.randrange(-300,212))

CreateTempConvTable(tempF)
