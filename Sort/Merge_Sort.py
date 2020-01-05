class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        self.mergeSort(A, 0, len(A))

    def mergeSort(self, A, start, end):
        if start < end - 1:
            mid = (start + end) // 2

            self.mergeSort(A, start, mid)
            self.mergeSort(A, mid, end)

            A[start:end] = self.mergeSortedArray(A[start:mid], A[mid:end])

    def mergeSortedArray(self, left, right):
        reslt = []
        a = b = 0
        llen, rlen = len(left), len(right)
        while a < llen and b < rlen:
            if left[a] <= right[b]:
                reslt.append(left[a])
                a += 1
            else:
                reslt.append(right[b])
                b += 1
        if a >= llen:
            for i in range(b, rlen):
                reslt.append(right[i])
        else:
            for i in range(a, llen):
                reslt.append(left[i])

        return reslt


if __name__ == "__main__":
    A = [7,8,0,3,9,11,15,1,2,1,4,5]
    B = Solution().sortIntegers2(A)
    print(B)