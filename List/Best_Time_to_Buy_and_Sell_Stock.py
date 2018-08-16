class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        profit = 0
        if prices:
            buy_min = prices[0]
            for i in range(1, len(prices)):
                if prices[i] < buy_min:
                    buy_min = prices[i]
                new_profit = prices[i] - buy_min
                if new_profit > profit:
                    profit = new_profit
        return profit


if __name__ == "__main__":
    prices = [3,2,3,1,2]
    reslt = Solution().maxProfit(prices)
    print(reslt)
