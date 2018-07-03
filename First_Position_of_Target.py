class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        right = len(nums) - 1
        left = 0

        if right == -1:
            return -1


        while left < right:

            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                right = mid

        if nums[left] == target:
            return left
        else:
            return -1


if __name__ == "__main__":
    test = Solution()
    indx = test.binarySearch([1, 2, 9, 9, 10], 9)
    print(indx)
