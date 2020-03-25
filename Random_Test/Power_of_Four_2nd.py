class Solution:
    """
    @param num: an integer
    @return: whether the integer is a power of 4
    """
    def isPowerOfFour(self, num):
        count = 0
        # check if there is only 1 bit set in num
        if num and not (num & num - 1):
            # count 0 bits before 1
            while num > 1:
                num >>= 1
                count += 1
            if count % 2 == 0:  # if even number of 0 bits, return true
                return True
        return False


print(Solution().isPowerOfFour(16))