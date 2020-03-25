class Solution:
    """
    @param Stock: Stock information
    @return: return id
    """
    def highestGrowth(self, Stock):
        returns = [[x[0], float(x[2]) / float(x[1]) - 1] for x in Stock]
        reslt = returns[0]
        for i in returns[1:]:
            if i[1] > reslt[1]:
                reslt = i
        return reslt[0]


print(Solution().highestGrowth([["a01","13.22","15.33"],["a02","13.22","14.22"]]))