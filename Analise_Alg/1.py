def x(n):
    i = 1
    while i <= n:
        j = 1
        while j <= i:
            print(i*j, end=' ')
            j+=1
        print()
        i +=1


x(3)