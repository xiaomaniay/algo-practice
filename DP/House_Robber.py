class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        if not A:
            return 0
        if len(A) < 2:
            return A[0]
        pre = 0
        curr = A[0]
        for i in range(1, len(A)):
            temp = pre
            pre = curr
            curr = max(temp + A[i], curr)
        return curr


if __name__ == "__main__":
    A = [5,8,1,1,4]
    reslt = Solution().houseRobber(A)
    print(reslt)