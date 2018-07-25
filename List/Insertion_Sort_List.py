class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The first node of linked list.
    @return: The head of linked list.
    """
    def insertionSortList(self, head):
        newHead = ListNode(0)
        newHead.next = head
        while head.next:
            # insertPoint = newHead
            # while insertPoint.next and insertPoint.next.val < head.val:
            #     insertPoint = insertPoint.next
            # if pre != insertPoint:
            #     pre.next = head.next
            #     head.next = insertPoint.next
            #     insertPoint.next = head
            #     head = pre.next
            # else:
            #     pre = head
            #     head = head.next
            if head.next.val < head.val:
                pre = newHead
                while pre.next.val < head.next.val:
                    pre = pre.next
                temp = head.next
                head.next = temp.next
                temp.next = pre.next
                pre.next = temp
            else:
                head = head.next

        return newHead.next


if __name__ == "__main__":
    a = ListNode(4)
    b = ListNode(19)
    c = ListNode(5)
    d = ListNode(-1)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    reslt = Solution().insertionSortList(a)
    while reslt:
        print((reslt.val))
        reslt = reslt.next


