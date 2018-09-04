class Solution:
    """
    @param arr: The given matrix
    @return: Return the mininum sum
    """
    def minimumSubmatrix(self, arr):
        if not arr:
            return None
        sum_arr = [[0 for r in range(len(arr[0]) + 1)] for c in range(len(arr) + 1)]
        for i in range(1, len(sum_arr)):
            for j in range(1, len(sum_arr[0])):
                sum_arr[i][j] = arr[i - 1][j - 1] \
                                + sum_arr[i - 1][j] \
                                + sum_arr[i][j - 1] \
                                - sum_arr[i - 1][j - 1]
        min_sub = float("inf")
        for m in range(0, len(sum_arr)):
            for n in range(m + 1, len(sum_arr)):
                sub_sum = []
                for h in range(1, len(sum_arr[0])):
                    sub_sum.append(sum_arr[n][h] - sum_arr[m][h])
                max_sum = 0
                for l in range(0, len(sub_sum)):
                    min_sub = sub_sum[l] - max_sum if (sub_sum[l] - max_sum) < min_sub else min_sub
                    if sub_sum[l] > max_sum:
                        max_sum = sub_sum[l]
        return min_sub


if __name__ == "__main__":
    arr = [[999834713,-124550735,105668787]]
    print(Solution().minimumSubmatrix(arr))