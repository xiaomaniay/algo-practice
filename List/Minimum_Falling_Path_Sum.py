class Solution:
    """
    @param A: the given array
    @return: the minimum sum of a falling path
    """
    def minFallingPathSum(self, A):
        n = len(A)
        path = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                if not i:
                    path[i][j] = A[i][j]
                else:
                    if not j:
                        min_pre = min(path[i - 1][j], path[i - 1][j + 1])
                    elif j == n - 1:
                        min_pre = min(path[i - 1][j], path[i - 1][j - 1])
                    else:
                        min_pre = min(path[i - 1][j], path[i - 1][j - 1], path[i - 1][j + 1])

                    path[i][j] = A[i][j] + min_pre

        min_path = path[n - 1][0]
        for i in range(1, n):
            if path[n - 1][i] < min_path:
                min_path = path[n - 1][i]

        return min_path


print(Solution().minFallingPathSum([[-62,-63,23,31],[-5,-82,52,76],[85,69,80,85],[8,-22,41,-45]]))