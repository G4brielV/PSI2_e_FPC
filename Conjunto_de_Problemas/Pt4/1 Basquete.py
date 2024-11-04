def basquete(cm):
    if cm > 1400:
        return 3
    elif cm > 800:
        return 2
    else:
        return 1


print(basquete(1400))