class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        profit = 0
        i, length = 0, len(prices)
        while i < length:
            buy_min = sell_max = prices[i]
            while i < length and prices[i] >= sell_max:
                sell_max = prices[i]
                i += 1
            profit += sell_max - buy_min
        return profit


if __name__ == "__main__":
    prices = [3,2,3,1,2]
    reslt = Solution().maxProfit(prices)
    print(reslt)
