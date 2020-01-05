# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    m = max(A)
    if m < 1:
        return 1
    temp = [0] * (m + 1)
    for i in range(len(A)):
        if A[i] > 0:
            temp[A[i]] = 1
    for i in range(1, m + 1):
        if not temp[i]:
            return i
    return m + 1


if __name__ == "__main__":
    A = [1, 3, 6]
    a = solution(A)
    print(a)
