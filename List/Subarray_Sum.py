class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        if not nums:
            return None
        hash_reslt = {0: -1}
        accu_sum = 0
        for i in range(0, len(nums)):
            accu_sum += nums[i]
            if accu_sum in hash_reslt:
                return [hash_reslt[accu_sum] + 1, i]
            hash_reslt[accu_sum] = i
        return [-1, -1]

