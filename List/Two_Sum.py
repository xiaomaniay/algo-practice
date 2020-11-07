class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        hash_reslt = {}
        for i in range(0, len(numbers)):
            if (target - numbers[i]) in hash_reslt:
                return [hash_reslt[target - numbers[i]], i]
            hash_reslt[numbers[i]] = i
        return [-1, -1]

    def twoSum2(self, numbers, target):  # practice
        hash = {}
        for i in range(len(numbers)):
            if target - numbers[i] in hash:
                return [hash[target - numbers[i]], i]
            hash[numbers[i]] = i
        return [-1, -1]

