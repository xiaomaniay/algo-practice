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
        # if not root:
        #     return []
        # nodes = [root]
        # reslt = [[root.val]]
        # while nodes:
        #     newListNode = []
        #     newListVal = []
        #     for element in nodes:
        #         if element.left:
        #             newListNode.append(element.left)
        #             newListVal.append(element.left.val)
        #         if element.right:
        #             newListNode.append(element.right)
        #             newListVal.append(element.right.val)
        #     if len(newListNode) > 0:
        #         reslt.append(newListVal)
        #     nodes = newListNode
        # return reslt
        depth, reslt = 0, []
        reslt = self.dfs(root, reslt, depth)
        return reslt

    def dfs(self, root, reslt, depth):
        if not root:
            return None
        if len(reslt) < depth + 1:
            reslt.append([])
        reslt[depth].append(root.val)
        self.dfs(root.left, reslt, depth + 1)
        self.dfs(root.right, reslt, depth + 1)
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