class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """
    # def majorityNumber(self, nums):
    #     hash_count = {}
    #     for i in range(len(nums)):
    #         if nums[i] in hash_count:
    #             hash_count[nums[i]] += 1
    #         else:
    #             hash_count[nums[i]] = 1
    #     max_count = len(nums) / 2
    #     for item in hash_count:
    #         if hash_count[item] >= max_count:
    #             return item

    def majorityNumber(self, nums):
        ele, count = nums[0], 1
        for i in range(1, len(nums)):
            if count == 0:
                ele = nums[i]
                count += 1
            else:
                if nums[i] == ele:
                    count += 1
                else:
                    count -= 1
        return ele


if __name__ == "__main__":
    nums = [1,1,1,1,2,2,2]
    print(Solution().majorityNumber(nums))


