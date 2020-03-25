class Solution:
    """
    @param a: the array a
    @return: return the maximum value
    """
    def getAnswer(self, a):
        cmax = 0
        for i in range(len(a) - 1):
            if a[i] % 2 == 1:
                for j in range(i + 1, len(a)):
                    if a[j] % 2 == 0:
                        cmax = max(a[j] - a[i], cmax)
        return cmax


print(Solution().getAnswer([83,41,46,32,20,11,100,11,14,23,41,94,66,38,98,7,14,90,84,41,75,47,13,52,28,74,45,76,43,56,73,46,43,25,40,40,73,49,19,45,79,71,47,76,30,32,3,33,99,34,51,57,12,38,23,23,83,83,5,11,95,33,47,78,35,8,83,1,96,44,67,83,82,60,35,78,77,34,88,53,4,31,76,87,2,51,3,58,93,66,16,10,99,24,8,28,71,15,22,98]))