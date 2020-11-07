class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # dummyHead = ListNode(0)
        # while head:
        #     temp = head.next
        #     head.next = dummyHead.next
        #     dummyHead.next = head
        #     head = temp
        # return dummyHead.next
        if not head:
            return head
        newHead = head
        while head.next:
            temp = head.next
            head.next = temp.next
            temp.next = newHead
            newHead = temp
        return newHead

    def reverse2(self, head):  # practice
        if not head:
            return head
        pre = head
        while head.next:
            temp = head.next
            head.next = temp.next
            temp.next = pre
            pre = temp
        return pre
