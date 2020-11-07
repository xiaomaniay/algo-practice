class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    # def mergeSortedArray(self, A, m, B, n):
    #     endpoint = m + n - 1
    #     a = m - 1
    #     b = n - 1
    #
    #     while a > -1 and b > - 1:
    #         if A[a] <= B[b]:
    #             A[endpoint] = B[b]
    #             b -= 1
    #         else:
    #             A[endpoint] = A[a]
    #             a -= 1
    #         endpoint -= 1
    #     A[:b + 1] = B[:b + 1]
    #
    #     return A

    def mergeSortedArray(self, A, m, B, n):
        endpoint = m + n - 1
        a = m - 1
        b = n - 1
        while a > -1 and b > -1:
            if A[a] <= B[b]:
                A[endpoint] = B[b]
                b -= 1
            else:
                A[endpoint] = A[a]
                a -= 1
            endpoint -= 1
        A[:b + 1] = B[:b + 1]
        return A

if __name__ == "__main__":
    test = Solution()
    A, m = [1,2,3,0,0], 3
    B, n = [4,5], 2
    print(test.mergeSortedArray(A, m, B, n))
