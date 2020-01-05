def min_abs_sum(A):

    abs_A = [abs(A[i]) for i in range(0, len(A))]
    s = sum(abs_A)
    temp = [0] * (s + 1)
    temp[0] = 1
    for i in range(0, len(A)):
        for j in range(s, -1, -1):
            if temp[j] == 1 and (j + A[i]) < s:
                temp[j + A[i]] = 1

    for i in range(s // 2, s + 1):
        if temp[i] == 1:
            return abs(s - 2 * i)


if __name__ == "__main__":
    A = [1, 4, -6]
    a = min_abs_sum(A)
    print(a)
