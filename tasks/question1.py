def getpower(x,n):
    a = 1
    for i in range(1,n+1):
        a = a*x
    print(a)
    return a

def calculate(x,n):
    if n == 1:
        return (1/getpower(x,1))
    else:
        return calculate(x,n-1) + (1/getpower(x,n))

answer = calculate(3,5)
print(answer)
