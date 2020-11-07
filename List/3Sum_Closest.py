class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    # def threeSumClosest(self, numbers, target):
    #     sorted_nums = self.merge_sort(numbers)
    #     s_diff = float("inf")
    #     for i in range(0, len(sorted_nums)):
    #         diff = target - sorted_nums[i]
    #         s_diff = self.two_sum_closest(sorted_nums[:i], diff, s_diff)
    #     return target + s_diff
    #
    # def two_sum_closest(self, nums, diff, s_diff):
    #     if nums:
    #         s, e = 0, len(nums) - 1
    #         while s is not e:
    #             s_diff = ((nums[s] + nums[e]) - diff) if abs((nums[s] + nums[e]) - diff) < abs(s_diff) else s_diff
    #             if (nums[s] + nums[e]) > diff: e -= 1
    #             elif (nums[s] + nums[e]) < diff: s += 1
    #             else: return 0
    #     return s_diff

    def threeSumClosest(self, numbers, target):
        diff = float('inf')
        if numbers:
            numbers = sorted(numbers)
            for i in range(len(numbers)):
                diff = self.two_sum(numbers[i + 1:], target - numbers[i], diff)
        return target - diff

    def two_sum(self, nums, target, pre_diff):
        if nums:
            l, r = 0, len(nums) - 1
            while l < r:
                if abs(target - nums[l] - nums[r]) < abs(pre_diff):
                    pre_diff = target - nums[l] - nums[r]
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    break
        return pre_diff


if __name__ == "__main__":
    a = [2,7,11,15]
    print(Solution().threeSumClosest(a, 7))