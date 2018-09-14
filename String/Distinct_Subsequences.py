class Solution:
    """
    @param: : A string
    @param: : A string
    @return: Count the number of distinct subsequences
    """

    def numDistinct(self, S, T):
        nums_pre = [1 for x in range(len(S) + 1)]
        nums = nums_pre.copy()
        nums[0] = 0
        for i in range(len(T)):
            for j in range(len(S)):
                if T[i] == S[j]:
                    nums[j + 1] = nums[j] + nums_pre[j]
                else:
                    nums[j + 1] = nums[j]
            nums_pre = nums.copy()
        return nums[-1]


if __name__ == "__main__":
    S = "rababb"
    T = "rab"
    print(Solution().numDistinct(S, T))