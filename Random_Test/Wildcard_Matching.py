class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        match_table = [[False for j in range(0, len(s) + 1)] for i in range(0, len(p) + 1)]
        match_table[0][0] = True
        for i in range(1, len(p) + 1):
            for j in range(0, len(s) + 1):
                if j == 0:
                    if p[i - 1] == "*":
                        match_table[i][j] = match_table[i - 1][j]
                else:
                    if (p[i - 1] == s[j - 1] or p[i - 1] == "?") and match_table[i - 1][j - 1] == 1:
                        match_table[i][j] = True
                    elif p[i - 1] == "*" and (match_table[i][j - 1] == 1 or match_table[i - 1][j] == 1 or match_table[i - 1][j - 1] == 1):
                        match_table[i][j] = True
                    else:
                        match_table[i][j] = False
        return match_table[len(p)][len(s)]


if __name__ == "__main__":
    s = ''
    p = '**'
    print(Solution().isMatch(s, p))
