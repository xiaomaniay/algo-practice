'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
B = []
S = []
try:
    while True:
        line = input()
        if line == 'END':
            break
        order = [i for i in line.split(' ')]
        if order[1] == 'B':
            B.append(order)
        if order[1] == 'S':
            S.append(order)
except EOFError:
    pass

B.sort(key=lambda x: int(x[-2]), reverse=True)
S.sort(key=lambda x: int(x[-2]))

B = [i[-1]+'@'+i[-2]+'#'+i[0] for i in B]
S = [i[-1]+'@'+i[-2]+'#'+i[0] for i in S]

print('B:', B, '\n')
print('S:', S)