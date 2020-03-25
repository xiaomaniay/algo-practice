'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

N = int('3')
nums = '5 4 1'
nums = [int(i) for i in nums.split(' ')]
min = nums[0]
for i in range(2, N):
    if nums[i] < min:
        min = nums[i]
print(min)
