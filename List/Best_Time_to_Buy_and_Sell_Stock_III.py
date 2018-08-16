class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        total_profit = 0
        first_profit = self.forward(prices)
        second_profit = self.backward(prices)
        for i in range(len(first_profit)):
            new_profit = first_profit[i]
            if i < len(second_profit):
                new_profit += second_profit[i]
            if new_profit > total_profit:
                total_profit = new_profit
        return total_profit

    def forward(self, prices):
        profit = [0]
        if prices:
            buy_min = prices[0]
            for i in range(1, len(prices)):
                if prices[i] < buy_min:
                    buy_min = prices[i]
                new_profit = prices[i] - buy_min
                if new_profit > profit[-1]:
                    profit.append(new_profit)
                else:
                    profit.append(profit[-1])
        return profit

    def backward(self, prices):
        profit = [0]
        if prices:
            sell_max = prices[len(prices) - 1]
            for i in range(len(prices) - 2, 0, -1):
                if prices[i] > sell_max:
                    sell_max = prices[i]
                new_profit = sell_max - prices[i]
                if new_profit > profit[0]:
                    profit.insert(0, new_profit)
                else:
                    profit.insert(0, profit[0])
        return profit


if __name__ == "__main__":
    prices = [3,2,6,5,0,3]
    reslt = Solution().maxProfit(prices)
    print(reslt)
