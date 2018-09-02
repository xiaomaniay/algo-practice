class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        sorted_nums = self.merge_sort(numbers)
        s_diff = float("inf")
        for i in range(0, len(sorted_nums)):
            diff = target - sorted_nums[i]
            s_diff = self.two_sum_closest(sorted_nums[:i], diff, s_diff)
        return target + s_diff

    def two_sum_closest(self, nums, diff, s_diff):
        if nums:
            s, e = 0, len(nums) - 1
            while s is not e:
                s_diff = ((nums[s] + nums[e]) - diff) if abs((nums[s] + nums[e]) - diff) < abs(s_diff) else s_diff
                if (nums[s] + nums[e]) > diff: e -= 1
                elif (nums[s] + nums[e]) < diff: s += 1
                else: return 0
        return s_diff

    def merge_sort(self, numbers):
        if len(numbers) > 1:
            mid = int(len(numbers) / 2)
            ll = self.merge_sort(numbers[:mid])
            rl = self.merge_sort(numbers[mid:])
            numbers = self.merge(ll, rl)
        return numbers

    def merge(self, ll, rl):
        l = []
        a = b = 0
        while a < len(ll) and b < len(rl):
            if ll[a] <= rl[b]:
                l.append(ll[a])
                a += 1
            else:
                l.append(rl[b])
                b += 1
        l += rl[b:] if b < len(rl) else ll[a:]
        return l


if __name__ == "__main__":
    a = [2,7,11,15]
    print(Solution().threeSumClosest(a, 0))