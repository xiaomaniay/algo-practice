class Solution:
    """
    @param s: A string
    @return: the length of last word
    """
    def lengthOfLastWord(self, s):
        rev_s = ''.join(reversed(s.strip()))
        i = 0
        while i < len(rev_s) and not rev_s[i].isspace():
            i += 1
        return i

if __name__ == "__main__":
    s = 'hello, world'
    print(Solution().lengthOfLastWord(s))
