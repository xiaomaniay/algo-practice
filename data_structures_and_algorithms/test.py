# def solution(X):
#     # write your code in Python 3.6
#     fib = [0, 1]
#     while (X < fib[0]) or (X > fib[1]):
#         temp = fib[0]
#         fib[0] = fib[1]
#         fib[1] = temp + fib[1]
#
#     return min(abs(X - fib[0]), abs(X - fib[1]))


# def solution(A):
#     # write your code in Python 3.6
#     cap = 5000 - A[0]
#     temp = sorted(A[1:])
#     count = 0
#     while cap >= 0:
#         if temp[count] > cap:
#             break
#         cap -= temp[count]
#         count += 1
#     return count


def solution(S):
    # write your code in Python 3.6
    num = int(S)
    hex = format(num, 'x')
    s = set(['a', 'b', 'c', 'd', 'e', 'f', '1', '0'])
    reslt = ''
    for i in range(0, len(hex)):
        temp = hex[i]
        if temp not in s:
            return "ERROR"
        if temp == '1':
            temp = 'I'
        if temp == '0':
            temp = 'O'
        reslt += temp
    return reslt.upper()


# def solution(A):
#     # write your code in Python 3.6
#     change = True
#     while change:
#         change = False
#         B = A
#         for i in range(1, len(A) - 1):
#             if (A[i] > max(A[i - 1], A[i + 1])):
#                 B[i] -= 1
#                 change = True
#             if (A[i] < min(A[i - 1], A[i + 1])):
#                 B[i] += 1
#                 change = True
#         A = B
#
#     return A


# def solution(S):
#     # write your code in Python 3.6
#     dp = [[0 for x in range(len(S) + 1)] for x in range(26)]
#     for i in range(0, len(S)):
#         if



# ord(A[i]) - 97


if __name__ == "__main__":
    A = [4650, 150, 150, 150, 50,0,0,0]
    S = 9
    a = solution(S)

    print(a)

