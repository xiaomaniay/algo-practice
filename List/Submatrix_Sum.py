class Solution:
    """
    @param: matrix: an integer matrix
    @return: the coordinate of the left-up and right-down number
    """
    def submatrixSum(self, matrix):
        if matrix:
            sum_matrix = [[0 for r in range(len(matrix[0]) + 1)] for c in range(len(matrix) + 1)]
            for i in range(1, len(matrix) + 1):
                for j in range(1, len(matrix[0]) + 1):
                    sum_matrix[i][j] = matrix[i - 1][j - 1] \
                                       + sum_matrix[i - 1][j] \
                                       + sum_matrix[i][j - 1] \
                                       - sum_matrix[i - 1][j - 1]
            for m in range(1, len(sum_matrix)):
                for n in range(m, len(sum_matrix)):
                    hash_sums = {0: 0}
                    for h in range(1, len(sum_matrix[0])):
                        diff = sum_matrix[n][h] - sum_matrix[m - 1][h]
                        if diff in hash_sums:
                            return [(m - 1, hash_sums[diff]), (n - 1, h - 1)]
                        hash_sums[diff] = h
        return None



# class Solution:
#     """
#     @param: matrix: an integer matrix
#     @return: the coordinate of the left-up and right-down number
#     """
#     def submatrixSum(self, matrix):
#         if len(matrix) > 0:
#             for i in range(0, len(matrix)):
#                 lst = []
#                 for j in range(i, len(matrix)):
#                     lst = self.add_matrix(lst, matrix[j])
#                     indx = self.subarray_sum(lst)
#                     if indx != [-1, -1]:
#                         return [(i, indx[0]), (j, indx[1])]
#         return None
#
#     """reduce matrix to list"""
#     def add_matrix(self, a, b):
#         if not a or not b:
#             return a or b
#         lst = []
#         for i in range(0, len(a)):
#             lst.append(a[i] + b[i])
#         return lst
#
#     """check whether there is subarray whose sum is zero"""
#     def subarray_sum(self, lst):
#         h_nums = {0: -1}
#         sub_sum = 0
#         for i in range(0, len(lst)):
#             sub_sum += lst[i]
#             if sub_sum in h_nums:
#                 return [h_nums[sub_sum] + 1, i]
#             h_nums[sub_sum] = i
#         return [-1, -1]


if __name__ == "__main__":
    m =[[1,1,1,1,1,1,1,1,1,1,1,-10,1,1,1,1,1,1,1,1,1,1,1]]
    print(Solution().submatrixSum(m))