class Solution:
    """
    @param n: Length of the array
    @param num: num array
    @param cost: cost array
    @return: nothing
    """
    def strangeSort(self, n, num, cost):
        # reslt = []
        # for i in range(len(cost)):
        #     cost[i] = (cost[i], i)
        # sorted_cost = cost.sort(key=lambda tup: tup[0])
        # for i in range(len(cost)):
        #     reslt.append(num[cost[i][1]])
        #
        # return reslt
        return [x[1] for x in sorted(zip(cost, num))]


print(Solution().strangeSort(5, [3,1,2,4,5], [1,2,3,4,5]))