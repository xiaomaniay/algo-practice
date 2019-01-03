def find_brute(T, P):
    n, m = len(T), len(P)
    for i in range(n - m + 1):
        j = 0
        while j < m and T[i + j] == P[j]:
            j += 1
        if j == m:
            return i
    return -1


def find_boyer_moore(T, P):
    n, m = len(T), len(P)
    if m == 0: return 0

    last = {}
    for k in range(m):
        last[P[k]] = k

    i, k = m - 1, m - 1
    while i < n:
        if T[i] == P[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(T[i], -1)
            i += m - min(k, j + 1)
            k = m - 1
    return -1

T = "abcdefghijk"
P = "fgh"

print(find_boyer_moore(T, P))