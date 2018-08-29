class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of linked list
    """
    def deleteDuplicates(self, head):
        newHead = pre = ListNode(0)
        pre.next = head
        while head and head.next:
            if head.val == head.next.val:
                pre.next = head.next
            else:
                pre = head
            head = head.next
        return newHead.next

