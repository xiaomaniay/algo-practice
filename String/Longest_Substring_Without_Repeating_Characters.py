class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        hash_pre = {}
        start, curr = 0, 0
        reslt = []
        while curr < len(s):
            if s[curr] in hash_pre and hash_pre[s[curr]] >= start:
                reslt.append(curr - start)
                start = hash_pre[s[curr]] + 1
            hash_pre[s[curr]] = curr
            curr += 1
        reslt.append(curr - start)
        return max(reslt)


if __name__ == "__main__":
    s = "aaaa"
    print(Solution().lengthOfLongestSubstring(s))