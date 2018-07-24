"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: a ListNode
    @return: a ListNode
    """
    def swapPairs(self, head):
        newHead = pre = ListNode(0)
        pre.next = head
        while head and head.next:
            tempHead = head.next
            head.next = tempHead.next
            tempHead.next = head
            pre.next = tempHead
            pre = head
            head = head.next
        return newHead.next
