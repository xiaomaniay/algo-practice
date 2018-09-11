class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        reslt = {tuple(s)}
        pre = reslt
        while len(pre) > 0:
            cur = set()
            for item in pre:
                increment = 1
                while increment < len(item):
                    for i in range(len(item) - increment):
                        if self.isPalindrome(item[i:(i + increment + 1)]):
                                temp = list(item)
                                temp[i:(i + increment + 1)] = ["".join(temp[i:(i + increment + 1)])]
                                if tuple(temp) not in reslt:
                                    cur.add(tuple(temp))
                    increment += 1
            reslt = reslt | cur
            pre = cur
        return [list(elem) for elem in reslt]

    def isPalindrome(self, s):
        start, end = 0, len(s) - 1
        while start < end:
            if not str.isalnum(s[start]):
                start += 1
                continue
            if not str.isalnum(s[end]):
                end -= 1
                continue
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True


if __name__ == "__main__":
    s = "aabab"
    print(Solution().partition(s))
