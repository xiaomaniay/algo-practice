class Solution:

    def partition(self, lst, left, right):
        m = left
        for k in range(left, right + 1):
            if lst[k] < lst[left]:
                m += 1
                lst[m], lst[k] = lst[k], lst[m]
        lst[left], lst[m] = lst[m], lst[left]
        print(m)
        return m

    """
    @param nums: A list of integers
    @return: An integer denotes the middle number of the array
    """
    def median(self, nums):

        lstLength = len(nums)
        print(lstLength)
        target = int((lstLength - 1) / 2)
        left, right = 0, lstLength - 1

        selectIndx = -1
        while selectIndx != target:
            if selectIndx > target:
                right = selectIndx - 1
            else:
                left = selectIndx + 1
            selectIndx = self.partition(nums, left, right)

        return nums[selectIndx]


if __name__ == "__main__":
    nums = [4, 5, 1, 2, 3]
    test = Solution()
    print(test.median(nums))