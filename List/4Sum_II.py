class Solution:
    """
    @param A: a list
    @param B: a list
    @param C: a list
    @param D: a list
    @return: how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero
    """
    def fourSumCount(self, A, B, C, D):
        count = 0
        h1, h2 = {}, {}
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] + B[j] in h1:
                    h1[A[i] + B[j]] += 1
                else:
                    h1[A[i] + B[j]] = 1
        for l in range(len(C)):
            for h in range(len(D)):
                if C[l] + D[h] in h2:
                    h2[C[l] + D[h]] += 1
                else:
                    h2[C[l] + D[h]] = 1
        for key in h2:
            if (0 - key) in h1:
                count += (h1[0 - key] * h2[key])
        return count


if __name__ == "__main__":
    A = [-1, -2]
    B = [1, 2]
    C = [-1,-2]
    D = [1,2]
    print(Solution().fourSumCount(A, B, C, D))
