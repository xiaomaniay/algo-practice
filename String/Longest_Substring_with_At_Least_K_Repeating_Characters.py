class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: return an integer
    """
    def longestSubstring(self, s, k):
        if not s:
            return 0
        reslt = 0
        hash_s = {}
        for i in range(len(s)):
            if s[i] in hash_s:
                hash_s[s[i]] += 1
            else:
                hash_s[s[i]] = 1
        splits = set()
        for item in hash_s:
            if hash_s[item] < k:
                splits.add(item)
        if not splits:
            return len(s)
        for i in range(len(s)):
            if s[i] in splits:
                s = s[:i] + " " + s[i + 1:]
        list_s = s.split(" ")
        for sub in list_s:
            temp = self.longestSubstring(sub, k)
            reslt = max(temp, reslt)
        return reslt


if __name__ == "__main__":
    s = "ababcb"
    k = 2
    print(Solution().longestSubstring(s, k))

