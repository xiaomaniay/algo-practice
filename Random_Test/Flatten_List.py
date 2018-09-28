class Solution(object):

    # @param nestedList a list, each element in the list
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        reslt = []
        if type(nestedList) == int:
            return [nestedList]
        for i in range(len(nestedList)):
            if type(nestedList[i]) == int:
                reslt.append(nestedList[i])
            else:
                reslt += self.flatten(nestedList[i])
        return reslt


if __name__ == "__main__":
    l = 10
    print(Solution().flatten(l))
