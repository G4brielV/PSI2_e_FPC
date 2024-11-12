def resto_div(x,y):
    if x == y:
        return 0

    elif x < y:
        return x

    else:
        return resto_div(x-y,y)


print(resto_div(3,2))