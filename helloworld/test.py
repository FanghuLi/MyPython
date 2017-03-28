
def fun(a):

    if a <= 2:
        return 1
    else:
        return fun(a - 1) + fun(a - 2)


print fun(35)