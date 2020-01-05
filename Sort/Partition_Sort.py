class Solution:
    """
    @param A: an integer array
    @return: nothing
    """

    def sortIntegers2(self, A):
        self.quickSort(A, 0, len(A))

    def quickSort(self, A, start, end):
        if start < end:
            pivot = start
            idx = pivot
            for i in range(idx + 1, end):
                if A[i] < A[pivot] and idx + 1 <= i:
                    idx += 1
                    A[i], A[idx] = A[idx], A[i]

            A[pivot], A[idx] = A[idx], A[pivot]

            self.quickSort(A, start, idx)
            self.quickSort(A, idx + 1, end)


if __name__ == "__main__":
    A = [3, 4, 5, 1, 2]
    Solution().sortIntegers2(A)
    print(A)
