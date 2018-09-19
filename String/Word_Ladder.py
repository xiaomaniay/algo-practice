class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        if start == end:
            return 1
        interim = {start}
        dict_set = set(dict)
        num_level = self.bfs(interim, end, dict_set)
        return num_level + 1 if num_level > 0 else 0

    def bfs(self, interim, end, dict):
        if not interim:
            return 0
        interim_next = set()
        used = set()
        for item in interim:
            if self.diff(item, end) == 1:
                return 1
            next_words = self.get_next(item)
            for word in next_words:
                if word in dict:
                    interim_next.add(word)
                    used.add(word)
        for word in used:
            if word in dict:
                dict.remove(word)
        num_level = self.bfs(interim_next, end, dict)
        return num_level + 1 if num_level > 0 else 0

    def diff(self, word1, word2):
        diff = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff += 1
        return diff

    def get_next(self, word):
        next_words = []
        for i in range(len(word)):
            for j in range(97, 123):
                next_words.append(word[:i] + chr(j) + word[i + 1:])
        return next_words


if __name__ == "__main__":
    start = "hit"
    end = "cog"
    dict = ["hot", "dot", "dog", "lot", "log"]
    print(Solution().ladderLength(start, end, dict))
