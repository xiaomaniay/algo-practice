class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if k == 0 or not s:
            return 0
        hash_pre = {}
        start = curr = 0
        result = 0
        while curr < len(s):
            if s[curr] not in hash_pre:
                if len(hash_pre) == k:
                    result = max(result, curr - start)
                    while len(hash_pre) == k:
                        start += 1
                        hash_pre[s[start - 1]] -= 1
                        if hash_pre[s[start - 1]] == 0:
                            hash_pre.pop(s[start - 1])
                hash_pre[s[curr]] = 1
            else:
                hash_pre[s[curr]] += 1
            curr += 1
        result = max(result, curr - start)
        return result


if __name__ == "__main__":
    s ="eqgkcwGFvjjmxutystqdfhuMblWbylgjxsxgnoh"
    print(Solution().lengthOfLongestSubstringKDistinct(s, 5))



