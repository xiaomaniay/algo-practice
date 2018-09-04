class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        indx = [0, 0]
        if nums:
            acc_sums = []
            hash_sums = {0: -1}
            sum = 0
            for i in range(len(nums)):
                sum += nums[i]
                acc_sums.append(sum)
                if sum in hash_sums:
                    return [hash_sums[sum] + 1, i]
                hash_sums[sum] = i
            s_acc_sums = sorted(acc_sums)
            diff = abs(s_acc_sums[0])
            indx = [0, hash_sums[s_acc_sums[0]]]
            for i in range(1, len(s_acc_sums)):
                new_diff = abs(s_acc_sums[i] - s_acc_sums[i - 1])
                if new_diff < diff:
                    a, b = hash_sums[s_acc_sums[i]], hash_sums[s_acc_sums[i - 1]]
                    indx = [a + 1, b] if a <= b else [b + 1, a]
                    diff = new_diff
        return indx