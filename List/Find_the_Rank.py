class Solution:
    """
    @param scores: two dimensional array
    @param K: a integer
    @return: return a integer
    """
    def FindTheRank(self, scores, K):
        total_scores = []
        for i in range(len(scores)):
            total_scores.append(sum(scores[i]))

        score = self.partition(total_scores[:], 0, len(scores), len(scores) - K)
        for i in range(len(scores)):
            if total_scores[i] == score:
                return i

    def partition(self, l, start, end, pos):
        pivot = start
        front = pivot
        for i in range(front + 1, len(l)):
            if l[i] < l[pivot] and front + 1 <= i:
                front += 1
                l[i], l[front] = l[front], l[i]
        l[pivot], l[front] = l[front], l[pivot]
        if front < pos:
            self.partition(l, front + 1, end, pos)
        if front > pos:
            self.partition(l, 0, front, pos)
        return l[pos]


print(Solution().FindTheRank([[96,0,82],[1,82,4],[93,83,15],[30,47,17],[79,79,71]], 2))

