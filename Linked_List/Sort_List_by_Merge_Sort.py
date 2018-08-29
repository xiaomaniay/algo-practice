class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def sortList(self, head):
        if not head or not head.next:
            return head
        leftHead = head
        mid = self.getMid(head)
        rightHead = mid.next
        mid.next = None
        leftHead = self.sortList(leftHead)
        rightHead = self. sortList(rightHead)

        return self.merge(leftHead, rightHead)

    def merge(self, leftHead, rightHead):
        dumHead = pre = ListNode(0)
        while leftHead and rightHead:
            if leftHead.val <= rightHead.val:
                pre.next = leftHead
                leftHead = leftHead.next
            else:
                pre.next = rightHead
                rightHead = rightHead.next
            pre = pre.next
        if leftHead:
            pre.next = leftHead
        else:
            pre.next = rightHead
        return dumHead.next

    def getMid(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(1)
    c = ListNode(1)
    d = ListNode(1)
    a.next = b
    b.next = c
    c.next = d
    reslt = Solution().sortList(a)
    print(reslt)

