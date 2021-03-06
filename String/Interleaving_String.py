class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    # def isInterleave(self, s1, s2, s3):
    #     if (len(s1) + len(s2)) != len(s3):
    #         return False
    #     a = b = c = 0
    #
    #     while a < len(s1) and b < len(s2) and c < len(s3):
    #         m1 = m2 = 0
    #         while a + m1 < len(s1) and s1[a + m1] == s3[c + m1]:
    #             m1 += 1
    #         while b + m2 < len(s2) and s2[b + m2] == s3[c + m2]:
    #             m2 += 1
    #         if m1 == m2 == 0:
    #             return False
    #         elif m1 >= m2:
    #             a += 1
    #             c += 1
    #         else:
    #             b += 1
    #             c += 1
    #     if s1[a:] == s3[c:] or s2[b:] == s3[c:]:
    #         return True
    #     else:
    #         return False
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        match_table = [[False for i in range(0, len(s2) + 1)] for j in range(0, len(s1) + 1)]
        match_table[0][0] = True
        for i in range(0, len(s1)):
            if s3[i] == s1[i] and match_table[i][0]:
                match_table[i + 1][0] = True
            else:
                break
        for j in range(0, len(s2)):
            if s3[j] == s2[j] and match_table[0][j]:
                match_table[0][j + 1] = True
            else:
                break
        for m in range(1, len(s1) + 1):
            for n in range(1, len(s2) + 1):
                if (s3[m + n - 1] == s1[m - 1] and match_table[m - 1][n]) \
                        or (s3[m + n - 1] == s2[n - 1] and match_table[m][n - 1]):
                    match_table[m][n] = True
        return match_table[len(s1)][len(s2)]










if __name__ == "__main__":
    s1 = "abcabc"
    s2 = "ac"
    s3 = "aabcabcc"
    print(Solution().isInterleave(s1, s2, s3))

