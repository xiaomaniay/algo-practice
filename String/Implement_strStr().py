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
            i = 0
            while i <= len(source) - len(target):
                j = 0
                while j < len(target):
                    if source[i + j] != target[j]:
                        break
                    else:
                        if j == len(target) - 1:
                            return i
                    j += 1
                i += 1
        return -1


if __name__ == "__main__":
    s = 'ABC'
    t = ''
    print(Solution().strStr(s, t))
