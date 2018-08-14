class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):

        nodes = [[root]]
        reslt = [[root.val]]
        for list in nodes:
            newListNode = []
            newListVal = []
            for element in list:
                if element.left:
                    newListNode.append(element.left)
                    newListVal.append(element.left.val)
                if element.right:
                    newListNode.append(element.right)
                    newListNode.append(element.right.val)
            if len(newListNode) > 0:
                nodes.append(newListNode)
                reslt.append(newListVal)

        return reslt



if __name__ == "__main__":
    a = TreeNode(10)
    b = TreeNode(9)
    c = TreeNode(8)
    d = TreeNode(7)
    e = TreeNode(4)
    f = TreeNode(6)
    a.left = b
    b.left = c
    c.left = d
    d.left = e
    e.right = f
    reslt = Solution().levelOrder(a)
    print(reslt)