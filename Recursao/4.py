def Ackerman(m,n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return Ackerman(m-1,1)
    else:
        return Ackerman(m-1,Ackerman(m,n-1))


print(Ackerman(1,2))