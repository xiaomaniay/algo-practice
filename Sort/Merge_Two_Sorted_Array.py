class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        reslt = []
        a = b = 0
        lenA, lenB = len(A), len(B)
        while a < lenA and b < lenB:
            if A[a] <= B[b]:
                reslt.append(A[a])
                a += 1
            else:
                reslt.append(B[b])
                b += 1
        if a >= lenA:
            for i in range(b, lenB):
                reslt.append(B[i])
        else:
            for i in range(a, lenA):
                reslt.append(A[i])

        return reslt

if __name__ == "__main__":
    test = Solution()
    A = []
    B = []
    print(test.mergeSortedArray(A, B))
