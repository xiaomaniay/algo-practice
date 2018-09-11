class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
        if not A or not B:
            return 0
        match_table = [[0 for i in range(0, len(B) + 1)] for j in range(0, len(A) + 1)]
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                a, b = A[i - 1], B[j - 1]
                if A[i - 1] == B[j - 1]:
                    match_table[i][j] = max(match_table[i - 1][j], match_table[i][j - 1], match_table[i - 1][j - 1] + 1)
                else:
                    match_table[i][j] = max(match_table[i - 1][j], match_table[i][j - 1], match_table[i - 1][j - 1])
        return match_table[len(A)][len(B)]


if __name__ == "__main__":
    A = "ABCD"
    B = "EACB"
    print(Solution().longestCommonSubsequence(A, B))


