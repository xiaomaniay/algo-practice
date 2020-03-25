class Solution:
    """
    @param funds: The investment each time
    @param a: The initial funds of A
    @param b: The initial funds of B
    @param c: The initial funds of C
    @return: The final funds
    """
    def getAns(self, funds, a, b, c):
        for i in range(len(funds)):
            if a <= b and a <= c:
                a += funds[i]
            elif b <= a and b <= c:
                b += funds[i]
            else:
                c += funds[i]

        return [a, b, c]


print(Solution().getAns([1,2,1,3,1,1], 1,2,1))


