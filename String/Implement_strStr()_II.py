class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr2(self, source, target):
        if target is None:
            return -1
        if target == "":
            return 0
        cur, i = 0, 0
        next_table = self.next(target)
        if source:
            while cur < len(source) and i < len(target):
                if i == -1 or source[cur] == target[i]:
                    i += 1
                    cur += 1
                else:
                    i = next_table[i]
        if i == len(target):
            return cur - i
        else:
            return -1

    def next(self, target):
        k, j = -1, 0
        next_table = [-1]
        while j < len(target):
            if k == -1 or target[k] == target[j]:
                k += 1
                j += 1
                next_table.append(k)
            else:
                k = next_table[k]
        return next_table


if __name__ == "__main__":
    source = "abcde"
    target = "e"
    print(Solution().strStr2(source, target))
