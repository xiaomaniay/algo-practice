class Solution:
    """
    @param s: A string
    @return: An integer
    """
    def minCut(self, s):
        if not s:
            return 0
        cut = [i - 1 for i in range(len(s) + 1)]
        is_palindrome = self.is_palindrome(s)
        for i in range(1 + len(s)):
            for j in range(i):
                a = s[j:i]
                if is_palindrome[j][i - 1]:
                    cut[i] = min(cut[i], 1 + cut[j])
        return cut[-1]

    def is_palindrome(self, s):
        is_palindrome = [[True for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s), -1, -1):
            for j in range(i, len(s)):
                if j == i:
                    is_palindrome[i][j] = True
                else:
                    is_palindrome[i][j] = s[i] == s[j] and is_palindrome[i + 1][j - 1]
        return is_palindrome

if __name__ == "__main__":
    s = "aaabaa"
    print(Solution().minCut(s))
