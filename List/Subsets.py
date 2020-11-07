class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):  # iteratively
        nums = sorted(nums)
        sets = [[]]
        for x in nums:
            new_sets =[]
            for set in sets:
                temp = set.copy()
                temp.append(x)
                new_sets.append(temp)

            sets += new_sets
        return sets

    def subsets2(self, nums):  # recursively
        nums = sorted(nums)

        def subsets(nums):
            if not nums:
                return [[]]
            sets = []
            new_sets = subsets(nums[:-1])
            for x in new_sets:
                temp = x.copy()
                temp.append(nums[-1])
                sets.append(temp)
            return sets + new_sets

        return subsets(nums)


print(Solution().subsets2([4,1,0]))

