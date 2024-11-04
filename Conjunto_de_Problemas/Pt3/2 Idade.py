def idade(mae,filho1,filho2):
    filho3 = mae - (filho1 + filho2)
    if filho3 > filho1 and filho3 > filho2:
        return filho3
    elif filho1 > filho2:
        return filho1
    else:
        return filho2


print(idade(47,21,9))