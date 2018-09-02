class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        reslts = set()
        if numbers:
            sorted_nums = sorted(numbers)
            pairs = self.pairs(sorted_nums)
            two_sums = self.two_sum([key for key in pairs.keys()], target)
            for two_sum in two_sums:
                for t1 in pairs[two_sum[0]]:
                    for t2 in pairs[two_sum[1]]:
                        if not set(t1).intersection(set(t2)):
                            a, b, c, d = sorted_nums[t1[0]], sorted_nums[t1[1]], sorted_nums[t2[0]], sorted_nums[t2[1]]
                            reslts.add(tuple(sorted([a, b, c, d])))
        return list(reslts)

    def pairs(self, nums):
        pairs = {}
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) in pairs:
                    pairs[nums[i] + nums[j]].append((i, j))
                else:
                    pairs[nums[i] + nums[j]] = [(i, j)]
        return pairs

    def two_sum(self, nums, target):
        two_sums, nums_set = set(), set()
        for i in range(0, len(nums)):
            if (target - nums[i]) in nums_set:
                two_sums.add((target - nums[i], nums[i]))
            nums_set.add(nums[i])
        return two_sums






if __name__ == "__main__":
    a = [1,-1,0,0,-2,2]
    print(Solution().fourSum(a, 0))