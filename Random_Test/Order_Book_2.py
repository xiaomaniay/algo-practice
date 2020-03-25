'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
B = []
S = []


def order_matching(order, B, S):
    if order[1] == 'B':
        i = 0
        while i < len(S):
            if S[i][-2] <= order[-2]:
                if S[i][-1] > order[-1]:
                    S[i][-1] -= order[-1]
                    return True
                elif S[i][-1] < order[-1]:
                    order[-1] -= S[i][-1]
                    S.remove(S[i])
                else:
                    S.remove(S[i])
                    return True
            else:
                return False
        return False
    if order[1] == 'S':
        i = 0
        while i < len(B):
            if B[i][-2] >= order[-2]:
                if B[i][-1] > order[-1]:
                    B[i][-1] -= order[-1]
                    return True
                elif B[i][-1] < order[-1]:
                    order[-1] -= B[i][-1]
                    B.remove(B[i])
                else:
                    B.remove(B[i])
                    return True
            else:
                return False
        return False


try:
    while True:
        line = input()
        if line == 'END':
            break
        order = [i for i in line.split(' ')]
        order[-1], order[-2] = int(order[-1]), int(order[-2])
        order_fulfilled = order_matching(order, B, S)
        if not order_fulfilled:
            if order[1] == 'B':
                if len(B) > 0:
                    for i in range(len(B)):
                        if B[i][-2] < order[-2]:
                            B.insert(i, order)
                            break
                        if i == len(B) - 1:
                            B.append(order)
                else:
                    B.append(order)
            if order[1] == 'S':
                if len(S) > 0:
                    for i in range(len(S)):
                        if S[i][-2] > order[-2]:
                            S.insert(i, order)
                            break
                        if i == len(S) - 1:
                            S.append(order)
                else:
                    S.append(order)
except EOFError:
    pass


B = [str(i[-1]) + '@' + str(i[-2]) + '#' + i[0] for i in B]
S = [str(i[-1]) + '@' + str(i[-2]) + '#' + i[0] for i in S]

print('B:', B, '\n')
print('S:', S)