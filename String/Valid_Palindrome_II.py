class Solution:
    """
    @param s: a string
    @return: nothing
    """
    def validPalindrome(self, s):
        start, end = 0, len(s) - 1
        del_flag = True
        while start < end:
            if s[start] != s[end]:
                if del_flag:
                    if s[start + 1] == s[end]:
                        start += 2
                        end += 1
                    elif s[start] == s[end - 1]:
                        start += 1
                        end -= 2
                    else:
                        return False
                    del_flag = False
                else:
                    return False
            start += 1
            end -= 1
        return True


if __name__ == "__main__":
    s = "abcab"
    print(Solution().validPalindrome(s))

