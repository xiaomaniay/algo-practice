class Solution:
    def findDuplicate(self, nums) -> int:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[j] == nums[i]:
                    return nums[i]
        return 0

print(Solution().findDuplicate([3,1,3,4,2]))