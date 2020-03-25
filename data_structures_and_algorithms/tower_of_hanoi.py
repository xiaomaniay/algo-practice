def hanoi(n, a, b, c):
    if n == 0:
        return
    else:
        hanoi(n - 1, a, c, b)
        print('Moving from a: ' + str(a) + ' to c: ' + str(c))
        c.append(a.pop())
        hanoi(n - 1, b, a, c)


hanoi(3, [3,2,1], [], [])



