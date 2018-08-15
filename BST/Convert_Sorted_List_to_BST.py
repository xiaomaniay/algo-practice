class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param: head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        if not head:
            return None
        pre, mid = self.findMid(head)
        rightHead = mid.next
        if pre == mid:
            head = None
        else:
            pre.next = None
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(rightHead)
        return root

    def findMid(self, head):
        pre = slow = head
        fast = head.next
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        return pre, slow


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    a.next = b
    b.next = c
    reslt = Solution().sortedListToBST(a)
    print(reslt)
