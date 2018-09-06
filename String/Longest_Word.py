class Solution:
    """
    @param: dictionary: an array of strings
    @return: an arraylist of strings
    """
    def longestWords(self, dictionary):
        lst = []
        max_length = 0
        for item in dictionary:
            if len(item) >= max_length:
                max_length = len(item)
                lst.append(item)
        return [lst[i] for i in range(0, len(lst)) if len(lst[i]) == max_length]


if __name__ == "__main__":
    dict = {"like", "love", "hate", "yes"}
    print(Solution().longestWords(dict))