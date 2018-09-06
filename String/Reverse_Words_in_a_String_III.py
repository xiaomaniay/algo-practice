class Solution:
    """
    @param s: a string
    @return: reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order
    """
    def reverseWords(self, s):
        i = 0
        while i < len(s):
            start = i
            while i < len(s) and not s[i].isspace():
                i += 1
            s = s[:start] + ''.join(reversed(s[start:i])) + s[i:]
            i += 1
        return s


if __name__ == "__main__":
    s = 'hello, world'
    print(Solution().reverseWords(s))



