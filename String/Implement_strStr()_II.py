class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        if not target:
            return 0
        if len(source) >= len(target):
            cur = 0
            partial_match = self.partial_match(target)
            while cur <= len(source) - len(target):
                for i in range(len(target)):
                    if source[i + cur] != target[i]:
                        cur += max(i - partial_match[i - 1], 1)
                        break
                else:
                    return cur
        return -1

    def next(self, target):
        i, j = -1, 0
        next = []
        while j < len(target):
            if i == -1 or target[i] == target[j]:
                i += 1; j += 1
                next.append(i)
            else:
                i = next[i]
        return next




if __name__ == "__main__":
    source = "abcde"
    target = "e"
    print(Solution().strStr(source, target))
