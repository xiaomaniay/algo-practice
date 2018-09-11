class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        lcp = ""
        if len(strs) > 0:
            for i in range(len(strs[0])):
                for j in range(1, len(strs)):
                    if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                        return lcp
                lcp += strs[0][i]
        return lcp

if __name__ == "__main__":
    A = []
    print(Solution().longestCommonPrefix(A))
