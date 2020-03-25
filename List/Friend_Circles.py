class Solution:
    def findCircleNum(self, M):

        disjoint_set = DisjointSet(len(M))

        for i in range(len(M)):
            for j in range(len(M)):  # M is symmetric
                if M[i][j] == 1:
                    disjoint_set.union(i, j)
        return disjoint_set.count


class DisjointSet:
    def __init__(self, n):
        self.set_id = [i for i in range(n)]
        self.set_size = [1 for _ in range(n)]
        self.count = n

    def find(self, i):
        while i is not self.set_id[i]:
            self.set_id[i] = self.set_id[self.set_id[i]]
            i = self.set_id[i]
        return i

    def union(self, i, j):
        p1 = self.find(i)
        p2 = self.find(j)
        if p1 == p2:
            return
        else:
            if self.set_size[p1] < self.set_size[p2]:
                self.set_id[p1] = self.set_id[p2]
                self.set_size[p2] += self.set_size[p1]
            else:
                self.set_id[p2] = self.set_id[p1]
                self.set_size[p1] += self.set_size[p2]
        self.count -= 1





M = [[1,1,0],[1,1,0],[0,0,1]]
print(Solution().findCircleNum(M))


