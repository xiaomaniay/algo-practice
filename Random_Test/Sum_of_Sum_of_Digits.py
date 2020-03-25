'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

N_Q = '5 5'
A = '13 345 193 44444 100303'
queries = ['1 2', '1 4', '2 1', '2 4', '1 5']
# try:
#     while True:
#         line = input()
#         queries.append(line)
# except EOFError:
#     pass

N_Q = [int(i) for i in N_Q.split(' ')]
N, Q = N_Q[0], N_Q[1]
A = [int(i) for i in A.split(' ')]


def sum_of_digits(x):
    if x < 10:
        return x
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum_of_digits(sum)


sums = []
for i in range(len(A)):
    sums.append(sum_of_digits(A[i]))
sums = sorted(sums)

reslt = []
for i in range(len(queries)):
    q = [int(j) for j in queries[i].split(' ')]
    if q[0] == 1:
        start = len(sums) - 1
        end = len(sums) - q[1] - 1
        step = -1
    if q[0] == 2:
        start = 0
        end = q[1]
        step = 1
    temp = 0
    for k in range(start, end, step):
        temp += sums[k]
    reslt.append(temp)

print('\n'.join(str(x) for x in reslt))