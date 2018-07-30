class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The head of linked list.
    @return: nothing
    """
    def reorderList(self, head):

        if not head or not head.next:
            return head

        mid = self.getMid(head)
        rightHead = self.reverse(mid.next)
        mid.next = None
        mergedHead = self.merge(head, rightHead)

        return mergedHead

    def merge(self, l1, l2):
        dumHead = pre = ListNode(0)
        while l1 or l2:
            if l1:
                pre.next = l1
                pre, l1 = pre.next, l1.next
            if l2:
                pre.next = l2
                pre, l2 = pre.next, l2.next
        return dumHead.next

    def reverse(self, head):
        rightHead = rightTail = head
        while rightTail.next:
            temp = rightTail.next
            rightTail.next = temp.next
            temp.next = rightHead
            rightHead = temp
        return rightHead

    def getMid(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == "__main__":
    a = ListNode(1)
    # b = ListNode(2)
    # c = ListNode(3)
    # d = ListNode(4)
    # a.next = b
    # b.next = c
    # c.next = d
    reslt = Solution().reorderList(a)
    print(reslt)