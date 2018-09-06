class Solution:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """
    # def anagram(self, s, t):
    #
    #     for i in range(0, len(s)):
    #         if s[i] in t:
    #             t = t.replace(s[i], '', 1)
    #         else:
    #             return False
    #     if t:
    #         return False
    #     return True

    def anagram(self, s, t):
        if len(s) != len(t):
            return False
        count_s = [0] * 26
        count_t = [0] * 26
        for i in range(0, len(s)):
            count_s[ord(s[i]) - ord('a')] += 1
            count_t[ord(t[i]) - ord('a')] += 1
        if count_s != count_t:
            return False
        else:
            return True


if __name__ == "__main__":
    s = 'ab '
    t = 'ac '
    print(Solution().anagram(s, t))
