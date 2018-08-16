class Solution:
    """
    @param K: An integer
    @param prices: An integer array
    @return: Maximum profit
    """
    def maxProfit(self, K, prices):
        total_profit, max_profit = [], 0
        total_profit = self.multi_trans(K, prices)
        for i in range(len(total_profit)):
            if total_profit[i] > max_profit:
                max_profit = total_profit[i]
        return max_profit

    def multi_trans(self, K, prices):
        total_profit = []
        first_profit = self.forward(prices)
        if (K - 1) > 1:
            second_profit = self.multi_trans(K - 1, prices[1:])
        elif (K - 1) == 1:
            second_profit = self.backward(prices)
        else:
            return first_profit
        for i in range(len(first_profit)):
            new_profit = first_profit[i]
            if i < len(second_profit):
                new_profit += second_profit[i]
            total_profit.append(new_profit)
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
    prices = [4,4,6,1,1,4,2,5]

    reslt = Solution().maxProfit(4,prices)
    print(reslt)
