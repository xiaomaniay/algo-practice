class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):

        # removeIndx = checkIndx = 0
        # lenA = len(A)
        #
        # while checkIndx < lenA:
        #     if A[checkIndx] != elem:
        #         A[removeIndx] = A[checkIndx]
        #         removeIndx += 1
        #     checkIndx += 1

        for a in A:
            if a == elem:
                A.remove(a)

        return len(A)


if __name__ == "__main__":
    test = Solution()
    A = [4, 5, 6, 9, 0 , 10, 14]
    elem = 0
    print(test.removeElement(A, elem))
