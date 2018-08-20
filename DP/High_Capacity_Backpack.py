class Solution:
    """
    @param s: The capacity of backpack
    @param v: The value of goods
    @param c: The capacity of goods
    @return: The answer
    """
    def getMaxValue(self, s, v, c):
        if not (v and c):
            return 0
        min_capacity, max_val = c[0], v[0]
        for i in range(1, len(c)):
            if c[i] < min_capacity:
                min_capacity = c[i]
                min_val = v[i]
        capacity = [0 for i in range(min_capacity, (s + 1))],
        capacity[0] = 1
        for i in range(len(c)):
            for j in range(len(capacity) - 1, -1, -1):
                if capacity[j] == 1:
                    if (j + c[i] + min_capacity) <= s:
                        capacity[j + c[i]] = 1

        return max_value


if __name__ == "__main__":
    s = 11
    v = [1,2,3]
    c = [3,5,7]
    reslt = Solution().getMaxValue(s, v, c)
    print(reslt)
