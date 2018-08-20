class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        if not A:
            return 0
        size = [0 for i in range(m)]
        size[0] = 1
        for i in range(len(A)):
            for j in range(len(size) - 1, - 1, - 1):
                if size[j] == 1:
                    if (j + A[i]) < m:
                        size[j + A[i]] = 1
                        continue
                    if (j + A[i]) == m:
                        return m
        for i in range(m - 1, - 1, - 1):
            if size[i] == 1:
                return i



if __name__ == "__main__":
    m = 11
    A = [2, 3, 5, 7]
    reslt = Solution().backPack(m, A)
    print(reslt)
