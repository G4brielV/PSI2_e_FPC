def xn(x,n):
    if n == 0:
        return 0
    else:
        return xn(x,n-1) + x


print(xn(20,5))