'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
q = '2'
n = ' 975 772'
q = int(q)
n = [int(i) for i in n.strip().split(' ')]
reslt = []

memo = {}


def check_palindrome(x):
    if x < 0 or (x > 0 and x % 10 == 0):
        return False
    back = 0
    while x > back:
        back = back * 10 + (x % 10)
        x = x // 10
    return x == back or x == (back // 10)


def form_palindrome(x, p):
    lst = list(x)
    palin = []
    for i in range(1, 3):
        combi = x
        for j in range(len(lst) - i, -1, -1):
            combi += lst[i]
            palin.append(int(combi))
    return palin


for i in range(len(n)):
    count = 0
    try:
        temp = 0
        power = len(str(n[i])) // 2
        j = n[i] // (10**power)
        key = 0
        for k in range(j, 0, -1):
            palin = form_palindrome(str(k), power)
            for p in palin:
                if p > n[i]:
                    continue
                if p in memo:
                    count += memo[p]
                    break
                if k == j:
                    key = p
                bin_rep = int("{0:b}".format(p))
                if check_palindrome(bin_rep):
                    temp += 1
            if count:
                break
        count += temp
        reslt.append(count)
        if key:
            memo[key] = count
    except Exception:
        print(i, j)


print(' '.join(str(x) for x in reslt))
