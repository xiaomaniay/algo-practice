'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
N_Q = '86 1'
A = '32 4 4 20 4 32 28 4 36 4 60 44 4 4 36 4 32 48 56 52 36 68 28 60 64 28 40 28 4 44 44 36 48 36 48 52 4 4 52 36 4 40 8 4 32 36 8 64 12 56 40 40 52 60 28 48 20 64 4 24 36 48 52 12 16 32 60 16 28 40 44 28 4 44 32 28 8 36 12 16 12 44 56 68 36 8'
index_lst = ['11 11']
try:
    while True:
        line = input()
        index_lst.append(line)
except EOFError:
    pass

memo = {1: 1, 2: 1}


def fibonacci(n):
    if n in memo:
        return memo[n]
    else:
        res = fibonacci(n-1) + fibonacci(n-2)
        memo[n] = res
        return memo[n]


def find_gcd(x, y):
    while (y):
        x, y = y, x % y

    return x


def gcd(l):
    if len(l) >= 2:
        reslt = [fibonacci(l[i]) for i in range(len(l))]
        while len(reslt) > 1:
            temp = []
            for i in range(0, len(reslt), 2):
                if i == len(reslt) - 1:
                    temp.append(reslt[i])
                else:
                    temp.append(find_gcd(reslt[i], reslt[i+1]))
            reslt = temp
        return reslt[0]
    return fibonacci(l[0])

N_Q = [int(i) for i in N_Q.split(' ')]
N = N_Q[0]
Q = N_Q[1]

A = [int(i) for i in A.split(' ')]

for i in range(Q):
    lst = index_lst[i]
    lst = [int(i) for i in lst.split(' ')]
    start = lst[0] - 1
    end = lst[1]
    print(gcd(A[start: end]))