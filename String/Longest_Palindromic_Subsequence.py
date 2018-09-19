class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longestPalindromeSubseq(self, s):
        if not s:
            return 0
        mat = [[0 for i in range(len(s))] for j in range(len(s))]
        for m in range(len(s) - 1, -1, -1):
            for n in range(m, len(s)):
                if m == n:
                    mat[m][n] = 1
                    continue
                if s[m] != s[n]:
                    mat[m][n] = max(mat[m + 1][n], mat[m][n - 1])
                if s[m] == s[n]:
                    mat[m][n] = max(mat[m + 1][n], mat[m][n - 1], mat[m + 1][n - 1] + 2)
        return mat[0][len(s) - 1]


if __name__ == "__main__":
    s = "bbaaaaaccbb"
    print(Solution().longestPalindromeSubseq(s))