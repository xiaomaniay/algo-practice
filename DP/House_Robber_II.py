class Solution:
    """
    @param nums: An array of non-negative integers.
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber2(self, nums):
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]
        curr_1 = self.houseRobber(nums[:(len(nums) - 1)])
        curr_2 = self.houseRobber(nums[1:])
        return max(curr_1, curr_2)

    def houseRobber(self, nums):
        pre = 0
        curr = nums[0]
        for i in range(1, len(nums)):
            temp = pre
            pre = curr
            curr = max(nums[i] + temp, curr)
        return curr


if __name__ == "__main__":
    A = [8,8,1]
    reslt = Solution().houseRobber2(A)
    print(reslt)