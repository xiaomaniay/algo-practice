class Solution:
    """
    @param K: An integer
    @param prices: An integer array
    @return: Maximum profit
    """
    def maxProfit(self, K, prices):
        total_profit = 0
        profits = self.max_tranc(prices)
        while K < len(profits):
            profits = self.less_tranc(profits)
        for profit in profits:
            total_profit += profit[2]
        return total_profit

    def less_tranc(self, profits): #reduce one tranction
        if len(profits) > 1:
            indx, min_profit = 0, profits[0][2]
            for i in range(1, len(profits)):
                if profits[i][2] < min_profit:
                    indx, min_profit = i, profits[i][2]

            profit_one = profit_two = 0
            if indx > 0:
                if (profits[indx][1] - profits[indx - 1][0]) > profits[indx - 1][2]:
                    profit_one = profits[indx][1] - profits[indx - 1][0]
            if indx < len(profits) - 1:
                if (profits[indx + 1][1] - profits[indx][0]) > profits[indx + 1][2]:
                    profit_two = profits[indx + 1][1] - profits[indx][0]
            if profit_one > profit_two:
                profits[indx - 1][1], profits[indx - 1][2] = profits[indx][1], profit_one
            if profit_two > profit_one:
                profits[indx + 1][0], profits[indx + 1][2] = profits[indx][0], profit_two
            del profits[indx]
        return profits

    def max_tranc(self, prices): #maximum tranctions that could happen
        profits = []
        i, length = 0, len(prices)
        while i < length:
            buy_min = sell_max = prices[i]
            while i < length and prices[i] >= sell_max:
                sell_max = prices[i]
                i += 1
            profit = sell_max - buy_min
            if profit > 0:
                profits.append([buy_min, sell_max, profit])
        return profits


if __name__ == "__main__":
    prices = [780,434,108,729,903,713,382,126,426,858,362,576,848,237,739,536,524,446,494,959,831,541,872,685,591,488,219,121,87,991]
    reslt = Solution().maxProfit(5, prices)
    print(reslt)
