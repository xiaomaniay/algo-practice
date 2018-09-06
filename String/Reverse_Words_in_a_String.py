class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        # rev_s = ''
        # i = 0
        # while i < len(s):
        #     word = ''
        #     while i < len(s) and not str.isspace(s[i]):
        #         word = word + s[i]
        #         i += 1
        #     rev_s = word + ' ' + rev_s
        #     while i < len(s) and str.isspace(s[i]):
        #         i += 1
        # return rev_s.strip()
        return ' '.join(reversed(s.strip().split()))


if __name__ == "__main__":
    s = "How are you?"
    print(Solution().reverseWords(s))