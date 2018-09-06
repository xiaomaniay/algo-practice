class Solution:
    """
    @param str: a string
    @return: return a string
    """
    def reverseWords(self, str):
        rev_str = ''.join(reversed(str))
        i = 0
        while i < len(str):
            start = i
            while i < len(str) and not rev_str[i].isspace():
                i += 1
            rev_str = rev_str[:start] + ''.join(reversed(rev_str[start:i])) + rev_str[i:]
            i += 1
        return rev_str


if __name__ == "__main__":
    s = 'hello, world'
    print(Solution().reverseWords(s))
