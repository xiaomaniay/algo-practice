class Solution:
    """
    @param num: an integer
    @return: whether the integer is a power of 4
    """
    def isPowerOfFour(self, num):
        if not num:  # return False if num is 0
            return False

        while num is not 1:
            if num % 4:
                return False
            num = num // 4
        return True


print(Solution().isPowerOfFour(64))