class Solution:
    """
    @param matrix: the given matrix
    @return: the largest possible sum
    """
    def maxSubmatrix(self, matrix):
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return 0
        sum_matrix = [[0 for i in range(len(matrix[0]) + 1)] for j in range(len(matrix) + 1)]
        for i in range(1, len(sum_matrix)):
            for j in range(1, len(sum_matrix[0])):
                sum_matrix[i][j] = matrix[i - 1][j - 1] \
                                   + sum_matrix[i - 1][j] \
                                   + sum_matrix[i][j - 1] \
                                   - sum_matrix[i - 1][j - 1]
        max_sub = float("-inf")
        for m in range(0, len(sum_matrix)):
            for n in range(m + 1, len(sum_matrix)):
                sub_sum = []
                for h in range(1, len(sum_matrix[0])):
                    sub_sum.append(sum_matrix[n][h] - sum_matrix[m][h])
                min_sum = 0
                for l in range(len(sub_sum)):
                    max_sub = sub_sum[l] - min_sum if (sub_sum[l] - min_sum) > max_sub else max_sub
                    if sub_sum[l] < min_sum:
                        min_sum = sub_sum[l]
        return max_sub


if __name__ == "__main__":
    arr = [[]]
    print(Solution().maxSubmatrix(arr))