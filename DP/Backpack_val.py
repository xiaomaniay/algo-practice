import sys

i = 0
limit = [10, 4]
value_l = [5,3,10,4]
weight_l = [4,2,8,8]

# for line in sys.stdin:
#     if i == 0:
#         l = list(line)
#         limit = [int(line[0]), int(line[1])]
#         i += 1
#         continue
#     value_l.append(int(line[0]))
#     weight_l.append(int(line[0]))
#     i += 1


def solution(W, weight, value, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weight[i - 1] <= w:
                K[i][w] = max(value[i - 1] + K[i - 1][w - weight[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]

print(solution(limit[0], weight_l, value_l, limit[1]), end="")