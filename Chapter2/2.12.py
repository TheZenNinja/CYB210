def Factorial(N):
    total = 1;
    for x in range(1,N+1):
        total*=x
    return total

num = int(input("get the factorial of: "))

print(Factorial(num))