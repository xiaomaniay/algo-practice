class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):

        lengthA = len(A)

        upperIndex = (lengthA - 1) if lengthA > 0 else 0
        lowerIndex = 0
        binIndex = (lowerIndex + upperIndex) // 2

        while A[binIndex] != target:

            if (upperIndex - lowerIndex) > 1:

                if A[binIndex] < target:
                    lowerIndex = binIndex + 1
                    upperIndex = max(upperIndex, lowerIndex)
                else:
                    upperIndex = binIndex - 1
                    lowerIndex = min(lowerIndex, upperIndex)

                binIndex = (lowerIndex + upperIndex) // 2

            else:
                if A[binIndex] < target:
                    return binIndex + 1
                else:
                    return binIndex

        return binIndex
