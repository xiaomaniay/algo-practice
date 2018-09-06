class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
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
    s = "121"
    print(Solution().isPalindrome(s))
