def par_impar(P,num1,num2):
    if (num1+num2)%2 == 0:
        return P

    else:
        if P == 0:
            return 1
        else:
            return 0


print(par_impar(0,0,3))
print(par_impar(1,0,3))
print(par_impar(0,1,5))