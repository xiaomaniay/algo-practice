class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        # arryLen = len(nums)
        # evenStartIndx = current = 0
        # while current <= arryLen - 1:
        #     temp = nums[current]
        #     if temp % 2 != 0:
        #         for i in range(current, evenStartIndx, -1):
        #             nums[i] = nums[i - 1]
        #         nums[evenStartIndx] = temp
        #         evenStartIndx += 1
        #     current += 1

        arryLen = len(nums)
        evenIndx, oddIndx = 0, arryLen - 1

        while evenIndx < oddIndx:
            checkEven, checkOdd = nums[evenIndx] % 2, nums[oddIndx] % 2
            if checkEven == 0 and checkOdd != 0:
                nums[evenIndx], nums[oddIndx] = nums[oddIndx], nums[evenIndx]
                evenIndx += 1
                oddIndx -= 1
            else:
                if checkEven != 0:
                    evenIndx += 1
                if checkOdd == 0:
                    oddIndx -= 1

        return nums


if __name__ == "__main__":
    test = Solution()
    print(test.partitionArray([402,455,25,15,42,538,369,741,651,473,310,112,525,682,622,119,287,242,701,439]))

