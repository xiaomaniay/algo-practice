class Solution:
    """
    @param A: A string
    @param B: A string
    @return: the length of the longest common substring.
    """

    def longestCommonSubstring(self, A, B):
        if not A or not B:
            return 0
        match_table = [[0 for i in range(len(B) + 1)] for j in range(len(A) + 1)]
        for m in range(1, len(A) + 1):
            for n in range(1, len(B) + 1):
                if A[m - 1] == B[n - 1]:
                    match_table[m][n] = match_table[m - 1][n - 1] + 1
        return max(max(match_table, key=lambda x: max(x)))



if __name__ == "__main__":
    A = "ABCD"
    B = "ABCE"
    print(Solution().longestCommonSubstring(A, B))
