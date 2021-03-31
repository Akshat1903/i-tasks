def series(a):
    for i in range(1,a+1):
        if(i%2 == 0):
            print((i*i)-1)
        else:
            print((i*i)+1)

# Number of terms in series including unknown = 9
series(9)
