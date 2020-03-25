N_M = '1 1'
A = '9'
queries = ['1 1']
# try:
#     while True:
#         line = input()
#         queries.append(line)
# except EOFError:
#     pass

N_M = [int(i) for i in N_M.split(' ')]
N, M = N_M[0], N_M[1]
A = [int(i) for i in A.split(' ')]

divisor_memo = {}
product_memo = {}


def number_of_divisors(x):
    if x in divisor_memo:
        return divisor_memo[x]
    count = 0
    sqrt_x = x**0.5
    i = 1
    while i <= sqrt_x:
        if x % i == 0:
            if i == sqrt_x:
                count += 1
            else:
                count += 2
        i += 1
    divisor_memo[x] = count
    return count


reslt = []
for i in range(len(queries)):
    q = [int(j) for j in queries[i].split(' ')]
    prod = 1
    for k in range(q[0] - 1, q[1]):
        prod *= A[k]
    # product_memo[(q[0], q[1])] = prod
    reslt.append(number_of_divisors(prod) % (10**9 + 7))

print('\n'.join(str(i) for i in reslt))
