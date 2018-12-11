def power(x, n):

    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)
        reslt = partial * partial
        if n % 2 == 1:
            reslt = reslt * x
    return reslt


print(power(2, 7), 2 ** 7)