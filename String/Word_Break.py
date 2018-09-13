class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        if not s:
            return True
        if not dict:
            return False
        long_word = max([len(item) for item in dict])
        mat = [False for str in range(len(s) + 1)]
        mat[0] = True
        for i in range(len(s)):
            for j in range(i, max(i - long_word, -1), -1):
                if s[j: i + 1] in dict and mat[j] == True:
                    mat[i + 1] = True
                    break
        return mat[-1]


if __name__ == "__main__":
    s = ""
    dict = []
    print(Solution().wordBreak(s, dict))

