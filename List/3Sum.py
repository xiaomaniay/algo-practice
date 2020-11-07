class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        reslt = set()
        numbers = sorted(numbers)
        for i in range(len(numbers)):
            if numbers[i] > 0:
                break
            two_sums = self.two_sum(numbers[i+1:], 0 - numbers[i])
            for j in two_sums:
                reslt.add((numbers[i], j[0], j[1]))
        return list(reslt)

    def two_sum(self, lst, target):
        reslt = set()
        pre = set()
        for i in range(len(lst)):
            if target - lst[i] in pre:
                reslt.add((target - lst[i], lst[i]))
            pre.add(lst[i])
        return reslt


if __name__ == "__main__":
    a = [-2,-3,5,-1,-4,5,-11,7,1,2,3,4,-7,-1,-2,-3,-4,-5]
    print(Solution().threeSum(a))
