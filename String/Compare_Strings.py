class Solution:
    """
    @param A: A string
    @param B: A string
    @return: if string A contains all of the characters in B return true else return false
    """
    def compareStrings(self, A, B):
        if len(A) < len(B):
            return False
        lst = [0] * 26
        for i in range(0, len(A)):
            lst[ord(A[i]) - ord('A')] += 1

        for j in range(0, len(B)):
            if lst[ord(B[j]) - ord('A')] <= 0:
                return False
            lst[ord(B[j]) - ord('A')] -= 1
        return True


if __name__ == "__main__":
    A = "ABCD"
    B = "ACD"
    print(Solution().compareStrings(A, B))
