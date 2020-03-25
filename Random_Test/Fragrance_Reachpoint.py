'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
first = '1 2'
second = '4 5'
N = '3'
xs = '2 5 7'
ys = '3 6 8'
num_query = '3'
ts = '1 6 15'

first = [int(i) for i in first.split(' ')]
second = [int(i) for i in second.split(' ')]
xs = [int(i) for i in xs.split(' ')]
ys = [int(i) for i in ys.split(' ')]
ts = [int(i) for i in ts.split(' ')]
N = int(N)
num_query = int(num_query)

first_t = [((first[0] - xs[i])**2 + (first[1] - ys[i])**2)**0.5 for i in range(N)]
second_t = [((second[0] - xs[i])**2 + (second[1] - ys[i])**2)**0.5 for i in range(N)]

counts = []
for i in range(num_query):
    temp = 0
    for j in range(N):
        if first_t[j] <= ts[i] and second_t[j] <= ts[i]:
            temp += 1
    counts.append(temp)

print(' '.join(str(x) for x in counts))