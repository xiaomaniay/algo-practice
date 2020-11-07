class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        if A:
            pivot = self.find_pivot(A, 0, len(A))
            if A[pivot] <= target <= A[len(A) - 1]:
                return self.find_target(A, pivot, len(A), target)
            else:
                return self.find_target(A, 0, pivot, target)
        return -1

    def find_target(self, A, start, end, target):
        if start < end - 1:
            mid = (start + end) // 2
            if A[mid] == target:
                return mid
            elif A[mid] > target:
                return self.find_target(A, start, mid, target)
            else:
                return self.find_target(A, mid + 1, end, target)

        return start if A[start] == target else -1

    def find_pivot(self, A, start, end):
        if start < end - 1:  # at least 2 elements
            mid = (start + end) // 2
            if mid == end - 1:
                return mid if A[mid] < A[mid - 1] else (mid - 1)
            if A[mid] < A[mid - 1] and A[mid] < A[mid + 1]:
                return mid
            else:
                if A[mid] < A[start] and A[mid] < A[end - 1]:
                    return self.find_pivot(A, start, mid)
                else:
                    return self.find_pivot(A, mid + 1, end)
        return start


A = [1002,10203,9,10,100,101]
print(Solution().search(A, 9))