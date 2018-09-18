class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        reslt = []
        if not strs:
            return reslt
        hash_strs = {}
        for i in range(len(strs)):
            key = [0 for x in range(26)]
            for j in range(len(strs[i])):
                key[ord(strs[i][j]) - 97] += 1
            if tuple(key) in hash_strs:
                hash_strs[tuple(key)].append(strs[i])
            else:
                hash_strs[tuple(key)] = [strs[i]]
        for item in hash_strs:
            if len(hash_strs[item]) > 1:
                reslt += hash_strs[item]
        return reslt

if __name__ == "__main__":
    strs = ["lint", "intl", "inlt", "code", "deoc"]
    print(Solution().anagrams(strs))
