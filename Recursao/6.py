def expo_recursivo(x,n):
    if n == 1:
        return x

    else:
        return expo_recursivo(x,n-1) * x


print(expo_recursivo(2,6))