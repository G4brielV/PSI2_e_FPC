def mdc(x,y):
    if x == y:
        return x

    elif x > y:
        return mdc(x-y, y)

    else:
        return mdc(y-x, x)


print(mdc(20,10))