class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        max_sum = curr = nums[0]
        for i in range(1, len(nums)):
            if curr < 0:
                curr = 0
            curr += nums[i]
            max_sum = max(max_sum, curr)
        return max_sum

    def maxSubArray2(self, nums):
        max_sum = curr = nums[0]
        for i in range(1, len(nums)):
            if curr < 0:
                curr = 0
            curr += nums[i]
            max_sum = max(max_sum, curr)
        return max_sum


if __name__ == "__main__":
    nums = [-2,2,-3,4,-1,2,1,-5,3]
    print(Solution().maxSubArray(nums))



