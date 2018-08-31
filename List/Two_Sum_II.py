class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        hash_reslt = {}
        for i in range(0, len(nums)):
            if (target - nums[i]) in hash_reslt:
                return [hash_reslt[target - nums[i]] + 1, i + 1]
            hash_reslt[nums[i]] = i
            i += 1
        return [-1, -1]
