class Solution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """
    def minDistance(self, word1, word2):
        dist_pre = [i for i in range(len(word1) + 1)]
        dist = dist_pre.copy()
        for i in range(len(word2)):
            dist[0] = i + 1
            for j in range(len(word1)):
                if word2[i] == word1[j]:
                    dist[j + 1] = dist_pre[j]
                else:
                    dist[j + 1] = min(dist_pre[j + 1], dist_pre[j], dist[j]) + 1
            dist_pre = dist.copy()
        return dist[-1]


if __name__ == "__main__":
    S = "rabbbb"
    T = "rab"
    print(Solution().minDistance(S, T))