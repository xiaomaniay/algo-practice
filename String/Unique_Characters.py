class Solution:
    """
    @param: str: A string
    @return: a boolean
    """
    def isUnique(self, str):
        hash_char = set()
        for i in range(0, len(str)):
            if str[i] in hash_char:
                return False
            hash_char.add(str[i])
        return True


if __name__ == "__main__":
    s = 'aab'
    print(Solution().isUnique(s))
