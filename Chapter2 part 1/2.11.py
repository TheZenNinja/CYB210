def AvgOf(N):
    total = 0;
    for x in range(N+1):
        total+=x
    return total

num = int(input("Input a number: "))

print(AvgOf(num))