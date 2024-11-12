def digitoK(num, digito):
    if num <= 0:
        return 0

    else:
        if digito == num%10:
            return 1 + digitoK(int(num/10), digito)

        else:
            return digitoK(int(num/10), digito)


print(digitoK(762021192, 2))