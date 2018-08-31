class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        reslts = set()
        sorted_numbers = self.merge_sort(numbers)
        for i in range(0, len(sorted_numbers)):
            two_sums = self.check(sorted_numbers[:i], 0 - sorted_numbers[i])
            if two_sums:
                for two_sum in two_sums:
                    reslts.add((two_sum[0], two_sum[1], sorted_numbers[i]))
        return list(reslts)

    def check(self, numbers, k):
        two_sums = set()
        nums_set = set()
        for i in range(0, len(numbers)):
            if (k - numbers[i]) in nums_set:
                two_sums.add((k - numbers[i], numbers[i]))
            nums_set.add(numbers[i])
        return two_sums

    def merge_sort(self, numbers):
        if len(numbers) > 1:
            mid = int(len(numbers)/2)
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
    a = [-2,-3,5,-1,-4,5,-11,7,1,2,3,4,-7,-1,-2,-3,-4,-5]
    print(Solution().threeSum(a))
