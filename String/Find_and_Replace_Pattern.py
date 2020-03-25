class Solution:
    """
    @param words: word list
    @param pattern: pattern string
    @return: list of matching words
    """
    def findAndReplacePattern(self, words, pattern):
        reslt = []
        for word in words:
            if len(word) is not len(pattern):
                continue
            bijection = {}
            is_matched = True
            for i in range(len(word)):
                if word[i] in bijection:
                    if bijection[word[i]] == pattern[i]:
                        continue
                    else:
                        is_matched = False
                elif pattern[i] in bijection.values():
                    is_matched = False
                else:
                    bijection[word[i]] = pattern[i]
            if is_matched:
                reslt.append(word)
        return reslt


words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = 'abb'
print(Solution().findAndReplacePattern(words, pattern))



