class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):

        right = len(A) - 1
        left = 0

        while left <= right:

            mid = (left + right) // 2

            if A[mid] < target:
                left = mid + 1
            elif A[mid] > target:
                right = mid - 1
            else:
                return mid

        return left


if __name__ == "__main__":
    test = Solution()
    indx = test.searchInsert([10, 15, 17], 9)
    print(indx)
