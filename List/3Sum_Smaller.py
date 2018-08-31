class Solution:
    """
    @param nums:  an array of n integers
    @param target: a target
    @return: the number of index triplets satisfy the condition nums[i] + nums[j] + nums[k] < target
    """
    def threeSumSmaller(self, nums, target):
        sorted_nums = self.merge_sort(nums)
        count = 0
        for i in range(0, len(sorted_nums)):
            diff = target - sorted_nums[i]
            count += self.two_sum_smaller(sorted_nums[:i], diff)
        return count

    def two_sum_smaller(self, nums, diff):
        sub_count = 0
        if nums:
            s, e = 0, len(nums) - 1
            while s is not e:
                if nums[s] + nums[e] < diff:
                    sub_count += (e - s)
                    s += 1
                else:
                    e -= 1
        return sub_count

    def merge_sort(self, nums):
        if len(nums) > 1:
            mid = int(len(nums)/2)
            ll = self.merge_sort(nums[:mid])
            rl = self.merge_sort(nums[mid:])
            nums = self.merge(ll, rl)
        return nums

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
        l += (ll[a:] or rl[b:])
        return l


if __name__ == "__main__":
    a = [-2,0,1,3]
    print(Solution().threeSumSmaller(a, 2))