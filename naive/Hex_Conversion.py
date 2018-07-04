class Solution:
    """
    @param n: a decimal number
    @param k: a Integer represent base-k
    @return: a base-k number
    """

    def hexConversion(self, n, k):
        res = ""

        if n == 0:
            return "0"
        else:
            while n:
                divRes = divmod(n, k)

                mod = divRes[1]

                if mod > 9:
                    mod = chr(ord("A") + mod - 10)
                else:
                    mod = str(divRes[1])

                res = mod + res

                n = divRes[0] if divRes[0] != 0 else None

        return res