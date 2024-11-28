def fatorial(n):

    if n == 1:
        return 1

    else:
        return n * fatorial(n-1)


def fib(num,a=0,b=1):

    if num == 1 or num == 2:
        return b+a

    else:
        return fib(num-1, a=b, b=a+b)

print(fib(7))