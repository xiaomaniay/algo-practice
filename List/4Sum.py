class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        reslts = set()
        s_nums = sorted(numbers)
        if s_nums:
            for i in range(0, len(s_nums)):
                if i != 0 and s_nums[i] == s_nums[i - 1]:
                    continue
                for j in range(i + 1, len(numbers)):
                    if j != i + 1 and s_nums[j] == s_nums[j - 1]:
                        continue
                    diff = target - (s_nums[i] + s_nums[j])
                    h_nums = set()
                    for l in range(j + 1, len(s_nums)):
                        if (diff - s_nums[l]) in h_nums:
                            reslts.add((s_nums[i], s_nums[j], diff - s_nums[l], s_nums[l]))
                        h_nums.add(s_nums[l])
        return list(reslts)


if __name__ == "__main__":
    a = [1,-1,0,0,-2,2]
    print(Solution().fourSum(a, 0))