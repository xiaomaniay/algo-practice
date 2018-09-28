class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """
    def minSubArray(self, nums):
        min_sum = curr = nums[0]
        for i in range(1, len(nums)):
            if curr > 0:
                curr = 0
            curr += nums[i]
            min_sum = min(min_sum, curr)
        return min_sum


if __name__ == "__main__":
    nums = [1, -1, -2, 1]
    print(Solution().minSubArray(nums))
