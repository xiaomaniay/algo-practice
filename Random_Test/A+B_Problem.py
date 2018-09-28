class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b
    """
    def aplusb(self, a, b):
        reslt = a ^ b
        carry = a & b
        carry <<= 1
        if carry != 0:
            reslt = self.aplusb(reslt, carry)
        return reslt


if __name__ == "__main__":
    a, b = 1, -10
    print(Solution().aplusb(a, b))