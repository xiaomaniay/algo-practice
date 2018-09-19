class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        if not s:
            return 0
        reslt = (0, 1)
        curr = 1
        while curr < len(s):
            i = 0
            while curr + i < len(s) and curr - 1 - i > -1 and s[curr + i] == s[curr - 1 - i]:
                i += 1
            reslt = (curr - i, curr + i) if 2 * i > (reslt[1] - reslt[0]) else reslt
            i = 0
            while curr + i < len(s) and curr - 2 - i > -1 and s[curr + i] == s[curr - 2 - i]:
                i += 1
            reslt = (curr - i - 1, curr + i) if 2 * i + 1 > (reslt[1] - reslt[0]) else reslt
            curr += 1
        return s[reslt[0]: reslt[1]]


if __name__ == "__main__":
    s = "aaaa"
    print(Solution().longestPalindrome(s))

