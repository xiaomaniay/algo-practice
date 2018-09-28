class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        if not nums:
            return None
        min_indx = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[min_indx]:
                min_indx = i
        temp = nums[:min_indx]
        for j in range(min_indx, len(nums)):
            nums[j - min_indx] = nums[j]
        nums[len(nums) - min_indx:] = temp
        return nums


if __name__ == "__main__":
    nums = [4, 5, 1, 2, 3]
    print(Solution().recoverRotatedSortedArray(nums))

