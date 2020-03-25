class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        match_table = [[False for i in range(0, len(s) + 1)] for j in range(0, len(p) + 1)]

        match_table[0][0] = True  # empty string is matched with empty string

        for i in range(1, len(p) + 1):
            for j in range(0, len(s) + 1):
                if j == 0:
                    if p[i - 1] == '*':
                        match_table[i][j] = match_table[i - 1][j]
                else:
                    if p[i - 1] == s[j - 1] or p[i - 1] == '?':
                        match_table[i][j] = match_table[i - 1][j - 1]
                    else:
                        if p[i - 1] == '*':
                            match_table[i][j] = match_table[i - 1][j] or match_table[i][j - 1]
                        else:
                            match_table[i][j] = False
        return match_table[len(p)][len(s)]


s = 'aaa'
p = '*a'
print(Solution().isMatch(s, p))


