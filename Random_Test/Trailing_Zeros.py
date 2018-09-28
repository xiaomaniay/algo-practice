class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        reslt = 0
        while n > 0:
            n = int(n / 5)
            reslt += n
        return reslt

if __name__ == "__main__":
    n = 51
    print(Solution().trailingZeros(n))




